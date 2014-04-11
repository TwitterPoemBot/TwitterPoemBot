#test class for the Poem model in the db schema
from poem import Poem, db
import unittest, logging, sys
class TestPoem(unittest.TestCase):
    #check and see if a Poem can be instantiated with the correct text
    def test_constructor(self):
        p = Poem("test")
        self.assertTrue(p.poemText == "test")

    def test_db(self):
        self.assertTrue(db != None)

    #check querying on the database
    def test_filter_by(self):
        p = Poem.query.filter_by(id=-1).first()
        self.assertTrue(p == None)

    #check and see if a poem can be saved to the db
    def test_save(self):
        p = Poem("lorem ipsum")
        Poem.save(p)
        db_poem = Poem.query.filter_by(id=p.id).first()
        self.assertTrue(p.id==db_poem.id)
        self.assertTrue(p.poemText == db_poem.poemText)

    #test if poems can be removed after saving
    def test_remove(self):
        p = Poem("lorem ipsum")
        Poem.save(p)
        db_poem = Poem.query.filter_by(id=p.id).first()
        self.assertTrue(p.id==db_poem.id)
        Poem.query.filter_by(id=p.id).delete()
        db_poem = Poem.query.filter_by(id=p.id).first()
        self.assertTrue(db_poem == None)

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    unittest.main()
