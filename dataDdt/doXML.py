from xml.etree import ElementTree

class ParseXml(object):
    def __init__(self, xmlpath):
        self.xmlpath = xmlpath

    # 获取根节点
    def getRoot(self):
        tree = ElementTree.parse(self.xmlpath)
        root = tree.getroot()
        return root

    # 根据根节点查找子节点
    def findNodeByName(self, parentNode, nodeName):
        nodes = parentNode.findall(nodeName)
        return nodes

    def getNodeOfChildText(self, node):
        # 获取节点node下所有子节点的节点名作为key
        # 本节点作为value组成的字典对象
        childrenTextDict = {}
        for i in list(node.iter())[1:]: # node 节点下的所有节点组成的列表
            childrenTextDict[i.tag] = i.text
        # print(list(node.iter())[1:])
        return childrenTextDict

    # 获取节点node下面的节点的所有数据
    def getDataFromXml(self, node):
        root = self.getRoot()
        books = self.findNodeByName(root, node)
        dataList=[]
        for book in books:
            childrentext = self.getNodeOfChildText(book)
            dataList.append(childrentext)
        return dataList
if __name__=='__main__':
    xml = ParseXml('./xmlData.xml')
    root = xml.getRoot()
    print(root.tag)
    books = xml.findNodeByName(root, 'book') # 查找所有的book节点
    for book in books:
        # print(book[0].tag, book[0].text)
        print(xml.getNodeOfChildText(book))
    print(xml.getDataFromXml('book'))