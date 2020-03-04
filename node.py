class binarynode:
    def __init__(self,quest,answ):
        self.question = quest
        self.answer = answ
        self.left_children = None  
        self.right_children = None

    def insertLeft(self, quest, ans):
        if self.left_children == None:
            self.left_children = binarynode(quest,ans)
        else:
            aux = binarynode(quest, ans)
            aux.left_children = self.left_children
            self.left_children = aux
    
    def insertRigth(self, quest, ans):
        if self.right_children == None:
            self.right_children = binarynode(quest, ans)
        else:
            aux = binarynode(quest, ans)
            aux.right_children = self.right_children
            self.right_children = aux
    
    def getLeftNode(self):
        return self.left_children

    def getRightNode(self):
        return self.right_children
    
    def getQuestion(self):
        return self.question
    
    def getAnswer(self):
        return self.answer
    
    def setLeftNode(self, node):
        self.left_children = node

    def setRightNode(self, node):
        self.right_children = node
    
    def setQuestion(self, ques):
        self.question =ques
    
    def setAnswer(self, answ):
        self.answer = answ
    
