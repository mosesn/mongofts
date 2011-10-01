class Mongofts(object):
      def __init__(self, coll):
            self.collection = coll

      def insert_text(self, text, payload):
            self.collection.insert({"text":text.split(),"payload":payload})

      def search_text_any(self, query):
            return [x["payload"] for x in self.collection.find({"text":{"$in":query.split()}})]

      def search_text_all(self, query):
            return [x["payload"] for x in self.collection.find({"text":{"$all":query.split()}})]
