import unittest

from src.ops.documents.search import find_first


class TestDocumentSearch(unittest.TestCase):

    def test_search_first_article(self):

        doc = {
            'document_name': 'doc',
            "nodes": [
                {
                    "key": "Article [3]",
                    "content": {
                        "meta": "Article",
                        "text": [
                            "86. Duty of local authority to consider needs of their area for further housing accommodation.."
                        ],
                        "id": "/root/part-1/chapter-2/article-3"
                    }
                }
            ]
        }

        result = find_first(doc, 'Article', '100.')
        self.assertTrue(result is None)

        doc = {
            'document_name': 'doc',
            "nodes": [
                {
                    "key": "Article [3]",
                    "content": {
                        "meta": "Article",
                        "text": [
                            "86. Duty of local authority to consider needs of their area for further housing accommodation.."
                        ],
                        "id": "/root/part-1/chapter-2/article-3"
                    }
                },
                {
                    "key": "Paragraph [6]",
                    "content": {
                        "meta": "Paragraph",
                        "text": [
                            "Paragraph 3.",
                            "(3)If the Secretary of State gives them notice to do so, they shall, within 3 months after such notice, prepare and submit to him proposals for the provision of housing accommodation."
                        ],
                        "id": "/root/part-1/chapter-2/article-3/paragraph-6"
                    }
                },
                {
                    "key": "Article [5]",
                    "content": {
                        "meta": "Article",
                        "text": [
                            "86. Duty of local authority to consider needs of their area for further housing accommodation.."
                        ],
                        "id": "/root/part-1/chapter-2/article-5"
                    }
                },
            ]
        }

        expected = "/root/part-1/chapter-2/article-3"
        result = find_first(doc, 'Article', '86')
        self.assertEqual(expected, result)



