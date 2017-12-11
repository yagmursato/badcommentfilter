import pandas
import numpy    as np
from pandas import DataFrame
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class NaiveBayes():
    def __init__(self):
        self.__bad_comments = []
        self.__good_comments = []
        self.__count = []
        self.__index = 0

    def readFiles(self, bad_file , good_file):
        with open(bad_file+".txt", "r") as f:
            for line in f:
                if len(line.split(" ")) > 5:
                    self.__bad_comments.append(line)
                    self.__count.append(self.__index)
                    self.__index += 1
        self.badLenght = self.__index

        with open(good_file+".txt", "r") as f:
            for line in f:
                if len(line.split(" ")) > 5:
                    self.__good_comments.append(line)
                    self.__count.append(self.__index)
                    self.__index += 1
        self.goodLenght = self.__index - self.badLenght

        return self.__bad_comments + self.__good_comments

    def __dataFrame(self):
        self.text = self.readFiles("kotuYorumlar","iyiYorumlar")
        if not self.__good_comments or not self.__bad_comments:
            raise BaseException("Read Files")

        self.data = {'text': self.text,'status': self.__count}
        self.frame = pandas.DataFrame(self.data)

        return self.frame["text"], self.frame["status"]

    def __train(self):
        self.vect = TfidfVectorizer(min_df=1)
        self.frame_x, self.frame_y = self.__dataFrame()
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.frame_x, self.frame_y, test_size=0.2, random_state=4)
        self.x_trainvect = self.vect.fit_transform(self.x_train)  # öğretitğimiz yer

    def __NaiveBayes(self):
        self.__train()
        self.mnb = MultinomialNB()
        self.y_train = self.y_train.astype('int')
        self.mnb.fit(self.x_trainvect, self.y_train)


    def test(self, sentence):
        self.__NaiveBayes()
        x_testvect = self.vect.transform([sentence])
        pred = self.mnb.predict(x_testvect)
        if pred[0] <= self.badLenght:
            return "Bad comment"
        else:
            return "Good comment"


a = NaiveBayes()
print(a.test("çok iyi mükemmel muhteşem bir haber"))



