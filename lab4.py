# -*- coding: utf-8 -*-
import xml.sax
class bookHandler( xml.sax.ContentHandler ):
    def __init__(self):
       print("init\n")
       self.CurrentData = ""
       self.author = ""
       self.title = ""
       self.year = ""
       self.price = ""
       self.publish_date = ""
       self.description = ""
    # Call when an element starts
    def startElement(self, tag, attributes):
        #print("startelement")
        self.CurrentData = tag
        if tag == "book":
            print(("*****book*****"))
            #print(type(attributes))
            #title = attributes["title"]
            #print("Title:", title)
    
    # Call when an elements ends
    def endElement(self, tag):
        #print("endelement\n")
        #x=self.__getattribute__(self.CurrentData)
        #print(f"{self.CurrentData}={x}")
        if self.CurrentData == "author":
            print("author:", self.author)
        elif self.CurrentData == "title":
            print("title:", self.title)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "price":
            print("price:", self.price)
        elif self.CurrentData == "publish_date":
            print("publish_date:", self.publish_date)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""
    
       # Call when a character is read
    def characters(self, content):
        #print("characters")
        #self.__setattr__(self.CurrentData,content)
        
        if self.CurrentData == "author":
           self.author = content
        elif self.CurrentData == "title":
           self.title = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "price":
            self.price = content
        elif self.CurrentData == "publish_date":
           self.publish_date = content
        elif self.CurrentData == "description":
           self.description = content
   
if ( __name__ == "__main__"):
    print("start")
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # override the default ContextHandler
    Handler = bookHandler()
    parser.setContentHandler( Handler )
    parser.parse("file.xml")
