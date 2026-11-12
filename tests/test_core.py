import unittest,copy,json
from sqlite_json_shape_lab import run
DEMO={'rows': [{'id': 'missing', 'doc': {}}, {'id': 'null', 'doc': {'x': None}}, {'id': 'string', 'doc': {'x': 'null'}}, {'id': 'bool', 'doc': {'x': True}}]}
class DomainTests(unittest.TestCase):
 def test_null_shape(self):
  x=run(DEMO)['rows'];self.assertIsNone(x[0]['json_type']);self.assertEqual(x[1]['json_type'],'null');self.assertIsNone(x[0]['sql_value']);self.assertIsNone(x[1]['sql_value'])
 def test_strings_and_booleans(self):
  x=run(DEMO)['rows'];self.assertEqual(x[2]['sql_type'],'text');self.assertEqual(x[3]['sql_value'],1);self.assertEqual(x[3]['json_type'],'true')
 def test_duplicate_ids(self):
  with self.assertRaises(ValueError):run({'rows':[DEMO['rows'][0]]*2})
