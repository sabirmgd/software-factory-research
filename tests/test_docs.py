from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_docs import check_links
from doc_utils import anchors,strip_fences
from render_diagrams import validate as validate_graph,mermaid

class DocumentationChecks(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.file=self.root/'README.md'
    def tearDown(self):self.temp.cleanup()
    def test_valid_relative_link_and_anchor(self):
        (self.root/'other.md').write_text('# Heading\n');self.file.write_text('[go](other.md#heading)')
        self.assertEqual(check_links(self.file,self.root),[])
    def test_broken_link_is_rejected(self):
        self.file.write_text('[bad](missing.md)');self.assertTrue(check_links(self.file,self.root))
    def test_unknown_anchor_is_rejected(self):
        (self.root/'other.md').write_text('# Heading\n');self.file.write_text('[bad](other.md#absent)')
        self.assertTrue(check_links(self.file,self.root))
    def test_fenced_examples_not_treated_as_real_links(self):
        self.file.write_text('```md\n[example](not-real.md)\n```\n')
        self.assertEqual(check_links(self.file,self.root),[])
    def test_external_urls_not_claimed_checked(self):
        self.file.write_text('[web](https://example.invalid/not-checked)')
        self.assertEqual(check_links(self.file,self.root),[])
    def test_explicit_source_anchor(self):
        self.file.write_text('<a id="s01"></a>\n[source](#s01)')
        self.assertEqual(check_links(self.file,self.root),[])
    def test_duplicate_heading_suffix(self):
        self.assertTrue({'same','same-1'}<=anchors('# Same\n\n# Same'))
    def test_link_cannot_escape_repo(self):
        self.file.write_text('[bad](../outside.md)');self.assertTrue(check_links(self.file,self.root))
    def test_nested_short_fence_does_not_end_long_fence(self):
        self.assertNotIn('hidden',strip_fences('````\n```\nhidden\n```\n````'))
    def test_diagram_rejects_unknown_node(self):
        with self.assertRaises(ValueError):validate_graph({'nodes':[{'id':'a'}],'edges':[{'from':'a','to':'b'}]})
    def test_diagram_rejects_duplicate_node(self):
        with self.assertRaises(ValueError):validate_graph({'nodes':[{'id':'a'},{'id':'a'}],'edges':[]})
    def test_mermaid_export_is_generated_from_labels(self):
        graph={'id':'test','nodes':[{'id':'a','label':'One\nTwo'}],'edges':[]}
        self.assertIn('One<br/>Two',mermaid(graph))
if __name__=='__main__':unittest.main()
