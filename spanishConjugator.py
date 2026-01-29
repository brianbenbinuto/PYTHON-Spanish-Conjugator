"""
Program: spanishConjugator.py
Author: Brian Erick Benbinuto
Date Created: October 9, 2023
Date Modified: October 10, 2023; October 11, 2023
The program drills the users on the Spanish conjugation of the present, pretérito indefinido, pretérito imperfecto, future, and conditional tenses.
It was based on the Java GUI program entitled SpanishConjugator.java created between October 5 and October 7, 2023.
"""

import random
import sys
from breezypythongui import EasyFrame

class SpanishConjugator(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title = "Spanish Conjugator", width = 810, height = 650)

        self.setResizable(False)

        self.numberScore = 0
        self.pronounList = ["Yo", "Tú", "Él", "Ella", "Usted", "Nosotros", "Nosotras", "Vosotros", "Vosotras", "Tú y yo", "Tú y él",
                                    "Tú y ella", "Ellos", "Ellas", "Ustedes"]
        self.conjugationSerList = ["SOY", "ERES", "ES", "ES", "ES", "SOMOS", "SOMOS", "SOIS", "SOIS", "SOMOS", "SOIS", "SOIS", "SON", 
                                            "SON", "SON"]
        self.conjugationEstarList = ["ESTOY", "ESTÁS", "ESTÁ", "ESTÁ", "ESTÁ", "ESTAMOS", "ESTAMOS", "ESTÁIS", "ESTÁIS", "ESTAMOS",
                                                "ESTÁIS", "ESTÁIS", "ESTÁN", "ESTÁN", "ESTÁN"]
        
        self.irregularVerbsList = ["IR", "SABER", "QUERER", "TENER", "DAR", "TRAER", "HACER" "PONER", "SALIR", "CONOCER", "CONDUCIR", "CONTRIBUIR",
                                   "DECIR"]
        self.conjugationQuererList = ["QUIERO", "QUIERES", "QUIERE", "QUIERE", "QUIERE", "QUEREMOS", "QUEREMOS", "QUERÉIS", "QUERÉIS",
                                                        "QUEREMOS", "QUERÉIS", "QUERÉIS", "QUIEREN", "QUIEREN", "QUIEREN"]
        self.conjugationIrList = ["VOY", "VAS", "VA", "VA", "VA", "VAMOS", "VAMOS", "VAIS", "VAIS", "VAMOS", "VAIS", "VAIS", "VAN",
                                                    "VAN", "VAN"]
        self.conjugationSaberList = ["SÉ", "SABES", "SABE", "SABE", "SABE", "SABEMOS", "SABEMOS", "SABÉIS", "SABÉIS", "SABEMOS",
                                                        "SABÉIS", "SABÉIS", "SABEN", "SABEN", "SABEN"]
        self.conjugationTenerList = ["TENGO", "TIENES", "TIENE", "TIENE", "TIENE", "TENEMOS", "TENEMOS", "TENÉIS", "TENÉIS",
                                                        "TENEMOS", "TENÉIS", "TENÉIS", "TIENEN", "TIENEN", "TIENEN"]
        self.conjugationDarList = ["DOY", "DAS", "DA", "DA", "DA", "DAMOS", "DAMOS", "DAIS", "DAIS", "DAMOS", "DAIS", "DAIS", "DAN", "DAN", "DAN"]
        self.conjugationTraerList = ["TRAIGO", "TRAES", "TRAE", "TRAE", "TRAE", "TRAEMOS", "TRAEMOS", "TRAÉIS", "TRAÉIS", "TRAEMOS", "TRAÉIS",
                                     "TRAÉIS", "TRAEN", "TRAEN", "TRAEN"]
        self.conjugationHacerList = ["HAGO", "HACES", "HACE", "HACE", "HACE", "HACEMOS", "HACEMOS", "HACÉIS", "HACÉIS", "HACEMOS", "HACÉIS", "HACÉIS",
                                     "HACEN", "HACEN", "HACEN"]
        self.conjugationPonerList = ["PONGO", "PONES", "PONE", "PONE", "PONE", "PONEMOS", "PONEMOS", "PONÉIS", "PONÉIS", "PONEMOS", "PONÉIS", "PONÉIS",
                                     "PONEN", "PONEN", "PONEN"]
        self.conjugationSalirList = ["SALGO", "SALES", "SALE", "SALE", "SALE", "SALIMOS", "SALIMOS", "SALÍS", "SALÍS", "SALIMOS", "SALÍS", "SALÍS", 
                                     "SALEN", "SALEN", "SALEN"]
        self.conjugationConocerList = ["CONOZCO", "CONOCES", "CONOCE", "CONOCE", "CONOCE", "CONOCEMOS", "CONOCEMOS", "CONOCÉIS", "CONOCÉIS", "CONOCEMOS",
                                       "CONOCÉIS", "CONOCÉIS", "CONOCEN", "CONOCEN", "CONOCEN"]
        self.conjugationConducirList = ["CONDUZCO", "CONDUCES", "CONDUCE", "CONDUCE", "CONDUCE", "CONDUCIMOS", "CONDUCIMOS", "CONDUCÍS", "CONDUCÍS",
                                        "CONDUCIMOS", "CONDUCÍS", "CONDUCÍS", "CONDUCEN", "CONDUCEN", "CONDUCEN"]
        self.conjugationContribuirList = ["CONTRIBUYO", "CONTRIBUYES", "CONTRIBUYE", "CONTRIBUYE", "CONTRIBUYE", "CONTRIBUIMOS", "CONTRIBUIMOS",
                                          "CONTRIBUÍS", "CONTRIBUÍS", "CONTRIBUIMOS", "CONTRIBUÍS", "CONTRIBUÍS", "CONTRIBUYEN", "CONTRIBUYEN", "CONTRIBUYEN"]
        self.conjugationDecirList = ["DIGO", "DICES", "DICE", "DICE", "DICE", "DECIMOS", "DECIMOS", "DECÍS", "DECÍS", "DECIMOS", "DECÍS", "DECÍS",
                                     "DICEN", "DICEN", "DICEN"] 

        self.regularVerbsList = ["HABLAR", "TOMAR", "COMER", "APRENDER", "VIVIR", "ABRIR", "DEBER"]
        self.endingsArPresentTenseList = ["O", "AS", "A", "A", "A", "AMOS", "AMOS", "ÁIS", "ÁIS", "AMOS", "ÁIS", "ÁIS", "AN", "AN", "AN"]
        self.endingsErPresentTenseList = ["O", "ES", "E", "E", "E", "EMOS", "EMOS", "ÉIS", "ÉIS", "EMOS", "ÉIS", "ÉIS", "EN", "EN", "EN"]
        self.endingsIrPresentTenseList = ["O", "ES", "E", "E", "E", "IMOS", "IMOS", "ÍS", "ÍS", "IMOS", "ÍS", "ÍS", "EN", "EN", "EN"]

        self.endingsArDefinitePastTenseList = ["É", "ASTE", "Ó", "Ó", "Ó", "AMOS", "AMOS", "ASTEIS", "ASTEIS", "AMOS", "ASTEIS", "ASTEIS", 
                                            "ARON", "ARON", "ARON"]
        self.endingsRestDefinitePastTenseList = ["Í", "ISTE", "IÓ", "IÓ", "IÓ", "IMOS", "IMOS", "ISTEIS", "ISTEIS", "IMOS", "ISTEIS", "ISTEIS", 
                                                "IERON", "IERON", "IERON"]
        self.endingsArImperfectPastTenseList = ["ABA", "ABAS", "ABA", "ABA", "ABA", "ÁBAMOS", "ÁBAMOS", "ABAIS", "ABAIS", "ÁBAMOS", "ABAIS", "ABAIS",
                                                                "ABAN", "ABAN", "ABAN"]
        self.endingsRestImperfectPastTenseList = ["ÍA", "ÍAS", "ÍA", "ÍA", "ÍA", "ÍAMOS", "ÍAMOS", "ÍAIS", "ÍAIS", "ÍAMOS", "ÍAIS", "ÍAIS", "ÍAN", "ÍAN", "ÍAN"]
        self.endingsFutureTenseList = ["É", "ÁS", "Á", "Á", "Á", "EMOS", "EMOS", "ÉIS", "ÉIS", "EMOS", "ÉIS", "ÉIS", "ÁN", "ÁN", "ÁN"]
        self.endingsConditionalTenseList = ["ÍA", "ÍAS", "ÍA", "ÍA", "ÍA", "ÍAMOS", "ÍAMOS", "ÍAIS", "ÍAIS", "ÍAMOS", "ÍAIS", "ÍAIS", "ÍAN", "ÍAN", "ÍAN"]
        
        self.intro = "Welcome to the Spanish Conjugator Program"
        self.message = self.addLabel(text = self.intro, row = 0, column = 0, columnspan = 2, font = ("Arial", 30), foreground = "maroon", background = "beige")
        self.score = self.addLabel(text = "Score: ", row = 1, column = 0, columnspan = 2, font = ("Arial", 25), foreground = "brown", background = "beige")

        self.setBackground("beige")

        self.conjugationSerButton = self.addButton(text = "Conjugation of Ser in the Present Tense", row = 2, column = 0, command = self.conjugationSerPresent)
        self.conjugationEstarButton = self.addButton(text = "Conjugation of Estar in the Present Tense", row = 2, column = 1, columnspan = 2, command = self.conjugationEstarPresent)
        self.conjugationIrregularPresentButton = self.addButton(text = "Conjugation of Irregular Verbs in the Present Tense", row = 3, column = 0, command = self.conjugationIrregularPresent)
        self.conjugationRegularPresentButton = self.addButton(text = "Conjugation of Regular Verbs in the Present Tense", row = 3, column = 1, command = self.conjugationRegularPresent)
        self.conjugationRegularDefinitePastButton = self.addButton(text = "Conjugation of Regular Verbs in the Pretérito Indefinido", row = 4, column = 0, command = self.conjugationRegularDefinitePast)
        self.conjugationRegularImperfectPastButton = self.addButton(text = "Conjugation of Regular Verbs in the Pretérito Imperfecto", row = 4, column = 1, command = self.conjugationRegularImperfectPast)
        self.conjugationRegularFutureButton = self.addButton(text = "Conjugation of Regular Verbs in the Future Tense", row = 5, column = 0, command = self.conjugationRegularFuture)
        self.conjugationRegularConditionalButton = self.addButton(text = "Conjugation of Regular Verbs in the Conditional Tense", row = 5, column = 1, command = self.conjugationRegularConditional)
        self.exitButton = self.addButton(text = "Exit", row = 6, column = 0, columnspan = 2, command = self.exit)

        self.label = self.addLabel(text = "Created by Brian Erick Benbinuto", row = 7, column = 0, columnspan = 2, font = ("Arial", 10), foreground = "brown", background = "beige")   

    def game1(self, infinitive, pronounList, verbList):

        while len(pronounList) != 0:
            index = random.randint(0, len(pronounList) - 1)

            self.answer = self.prompterBox(title = "Conjugation of " + infinitive, promptString = "How do you conjugate this verb?\n" + pronounList[index] + " " + "(" + infinitive + ")")
            self.answerUpperCase = self.answer.upper()

            numberOfGuesses = 0

            while (self.answerUpperCase != verbList[index] and numberOfGuesses <= 2):
                self.answer = self.prompterBox(title = "Conjugation of " + infinitive, promptString = "How do you conjugate this verb?\n" + pronounList[index] + " " + "(" + infinitive + ")")
                self.answerUpperCase = self.answer.upper()
                numberOfGuesses += 1
            
            if (self.answerUpperCase == verbList[index]):
                self.numberScore += 1
                self.score["text"] = "Score: " + str(self.numberScore)
                self.messageBox(title = "Spanish Conjugator", message = "That's right!\n\n" + pronounList[index] + " " + verbList[index])
            else:
                self.messageBox(title = "Spanish Conjugator", message = "That's wrong!\n\n" + pronounList[index] + " " + verbList[index])

            del pronounList[index]
            del verbList[index]

        self.messageBox(title = "Spanish Conjugator", message = "That's the end. Go back to Main Menu")
    
    def game2(self, pronounList, conjugation, mainVerb):

        while len(pronounList) != 0:
            index = random.randint(0, len(pronounList) - 1)

            self.answer = self.prompterBox(title = "Conjugation of " + mainVerb, promptString = "How do you conjugate this verb?\n" + pronounList[index] + " " + "(" + mainVerb + ")")
            self.answerUpperCase = self.answer.upper()

            numberOfGuesses = 0

            while (self.answerUpperCase != conjugation[index] and numberOfGuesses <= 2):
                self.answer = self.prompterBox(title = "Conjugation of " + mainVerb, promptString = "How do you conjugate this verb?\n" + pronounList[index] + " " + "(" + mainVerb + ")")
                self.answerUpperCase = self.answer.upper()
                numberOfGuesses += 1
            
            if (self.answerUpperCase == conjugation[index]):
                self.numberScore += 1
                self.score["text"] = "Score: " + str(self.numberScore)
                self.messageBox(title = "Spanish Conjugator", message = "That's right!\n\n" + pronounList[index] + " " + conjugation[index])
            else:
                self.messageBox(title = "Spanish Conjugator", message = "That's wrong!\n\n" + pronounList[index] + " " + conjugation[index])

            del pronounList[index]
            del conjugation[index]

        self.messageBox(title = "Spanish Conjugator", message = "That's the end for " + mainVerb + ".")

    def game3(self, pronounList, stem, conjugationEnding, mainVerb):

        while (len(pronounList) != 0):
            index = random.randint(0, len(pronounList) - 1)
            self.answer = self.prompterBox(title = "Conjugation of " + mainVerb, promptString = "How do you conjugate this verb?\n" + pronounList[index] + " " + "(" + mainVerb + ")")
            self.answerUpperCase = self.answer.upper()

            self.correctAnswer = stem + conjugationEnding[index]
            self.correctAnswer = self.correctAnswer.upper()

            numberOfGuesses = 0

            while (self.answerUpperCase != self.correctAnswer and numberOfGuesses <= 2):
                self.answer = self.prompterBox(title = "Conjugation of " + mainVerb, promptString = "How do you conjugate this verb?\n" + pronounList[index] + " " + "(" + mainVerb + ")")
                self.answerUpperCase = self.answer.upper()
                numberOfGuesses += 1
            
            if (self.answerUpperCase == self.correctAnswer):
                self.numberScore += 1
                self.score["text"] = "Score: " + str(self.numberScore)
                self.messageBox(title = "Spanish Conjugator", message = "That's right!\n\n" + pronounList[index] + " " + self.correctAnswer)
            else:
                self.messageBox(title = "Spanish Conjugator", message = "That's wrong!\n\n" + pronounList[index] + " " + self.correctAnswer)

            del pronounList[index]
            del conjugationEnding[index]

        self.messageBox(title = "Spanish Conjugator", message = "That's the end for " + mainVerb + ".")
    

    def game4(self, pronounList, conjugationEnding, mainVerb):

        while (len(pronounList) != 0):
            index = random.randint(0, len(pronounList) - 1)
            self.answer = self.prompterBox(title = "Conjugation of " + mainVerb, promptString = "How do you conjugate this verb?\n" + pronounList[index] + " " + "(" + mainVerb + ")")
            self.answerUpperCase = self.answer.upper()

            self.correctAnswer = mainVerb + conjugationEnding[index]
            self.correctAnswer = self.correctAnswer.upper()

            numberOfGuesses = 0

            while (self.answerUpperCase != self.correctAnswer and numberOfGuesses <= 2):
                self.answer = self.prompterBox(title = "Conjugation of " + mainVerb, promptString = "How do you conjugate this verb?\n" + pronounList[index] + " " + "(" + mainVerb + ")")
                self.answerUpperCase = self.answer.upper()
                numberOfGuesses += 1
            
            if (self.answerUpperCase == self.correctAnswer):
                self.numberScore += 1
                self.score["text"] = "Score: " + str(self.numberScore)
                self.messageBox(title = "Spanish Conjugator", message = "That's right!\n\n" + pronounList[index] + " " + self.correctAnswer)
            else:
                self.messageBox(title = "Spanish Conjugator", message = "That's wrong!\n\n" + pronounList[index] + " " + self.correctAnswer)

            del pronounList[index]
            del conjugationEnding[index]

        self.messageBox(title = "Spanish Conjugator", message = "That's the end for " + mainVerb + ".")
    
    def conjugationSerPresent(self):

        mainVerb = "SER"
        temporaryPronounList = self.pronounList.copy()
        temporaryConjugationSerList = self.conjugationSerList.copy()

        self.numberScore = 0
        self.score["text"] = "Score: " + str(self.numberScore)

        self.game1(mainVerb, temporaryPronounList, temporaryConjugationSerList)
    
    def conjugationEstarPresent(self):

        mainVerb = "ESTAR"
        temporaryPronounList = self.pronounList.copy()
        temporaryConjugationEstarList = self.conjugationEstarList.copy()

        self.numberScore = 0
        self.score["text"] = "Score: " + str(self.numberScore)

        self.game1(mainVerb, temporaryPronounList, temporaryConjugationEstarList)

    def conjugationIrregularPresent(self):

        temporaryIrregularVerbsList = self.irregularVerbsList.copy()

        self.numberScore = 0
        self.score["text"] = "Score: " + str(self.numberScore)

        while len(temporaryIrregularVerbsList) != 0:

            temporaryPronounList = self.pronounList.copy()
            temporaryConjugationQuererList = self.conjugationQuererList.copy()
            temporaryConjugationTenerList = self.conjugationTenerList.copy()
            temporaryConjugationIrList = self.conjugationIrList.copy()
            temporaryConjugationSaberList = self.conjugationSaberList.copy()
            temporaryConjugationDarList = self.conjugationDarList.copy()
            temporaryConjugationTraerList = self.conjugationTraerList.copy()
            temporaryConjugationHacerList = self.conjugationHacerList.copy()
            temporaryConjugationPonerList = self.conjugationPonerList.copy()
            temporaryConjugationSalirList = self.conjugationSalirList.copy()
            temporaryConjugationConocerList = self.conjugationConocerList.copy()
            temporaryConjugationConducirList = self.conjugationConducirList.copy()
            temporaryConjugationContribuirList = self.conjugationContribuirList.copy()
            temporaryConjugationDecirList = self.conjugationDecirList.copy()

            index = random.randint(0, len(temporaryIrregularVerbsList) - 1)

            if temporaryIrregularVerbsList[index] == "SABER":
                self.game2(temporaryPronounList, temporaryConjugationSaberList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "QUERER":
                self.game2(temporaryPronounList, temporaryConjugationQuererList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "TENER":
                self.game2(temporaryPronounList, temporaryConjugationTenerList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "IR":
                self.game2(temporaryPronounList, temporaryConjugationIrList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "DAR":
                self.game2(temporaryPronounList, temporaryConjugationDarList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "TRAER":
                self.game2(temporaryPronounList, temporaryConjugationTraerList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "HACER":
                self.game2(temporaryPronounList, temporaryConjugationHacerList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "PONER":
                self.game2(temporaryPronounList, temporaryConjugationPonerList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "SALIR":
                self.game2(temporaryPronounList, temporaryConjugationSalirList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "CONOCER":
                self.game2(temporaryPronounList, temporaryConjugationConocerList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "CONDUCIR":
                self.game2(temporaryPronounList, temporaryConjugationConducirList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "CONTRIBUIR":
                self.game2(temporaryPronounList, temporaryConjugationContribuirList, temporaryIrregularVerbsList[index])
            elif temporaryIrregularVerbsList[index] == "DECIR":
                self.game2(temporaryPronounList, temporaryConjugationDecirList, temporaryIrregularVerbsList[index])
            
            del temporaryIrregularVerbsList[index]

            if len(temporaryIrregularVerbsList) != 0:

                decision = self.prompterBox(title = "Continue?", promptString = "Do you want to continue?" +
                                                "\nType y or Y if yes. Otherwise, type n or N if no.")
                decision = decision.upper()

                if decision == "Y":
                    continue
                elif decision == "N":
                    break

    def conjugationRegularPresent(self):
        self.numberScore = 0
        self.score["text"] = "Score: " + str(self.numberScore)

        temporaryRegularVerbsList = self.regularVerbsList.copy()

        while len(temporaryRegularVerbsList) != 0:
            temporaryPronounList = self.pronounList.copy()
            temporaryEndingsArPresentTenseList = self.endingsArPresentTenseList.copy()
            temporaryEndingsErPresentTenseList = self.endingsErPresentTenseList.copy()
            temporaryEndingsIrPresentTenseList = self.endingsIrPresentTenseList.copy()

            index = random.randint(0, len(temporaryRegularVerbsList) - 1)

            verb = temporaryRegularVerbsList[index]
            stem = verb[0: len(temporaryRegularVerbsList[index]) - 2]
            ending = verb[len(temporaryRegularVerbsList[index]) - 2:]

            if (ending == "AR"):
                self.game3(temporaryPronounList, stem, temporaryEndingsArPresentTenseList, temporaryRegularVerbsList[index])
            elif (ending == "ER"):
                self.game3(temporaryPronounList, stem, temporaryEndingsErPresentTenseList, temporaryRegularVerbsList[index])
            elif (ending == "IR"):
                self.game3(temporaryPronounList, stem, temporaryEndingsIrPresentTenseList, temporaryRegularVerbsList[index])

            del temporaryRegularVerbsList[index]

            if len(temporaryRegularVerbsList) != 0:

                decision = self.prompterBox(title = "Continue?", promptString = "Do you want to continue?" +
                                                "\nType y or Y if yes. Otherwise, type n or N if no.")
                decision = decision.upper()

                if decision == "Y":
                    continue
                elif decision == "N":
                    break

    def conjugationRegularDefinitePast(self):
        self.numberScore = 0
        self.score["text"] = "Score: " + str(self.numberScore)

        temporaryRegularVerbsList = self.regularVerbsList.copy()

        while len(temporaryRegularVerbsList) != 0:
            temporaryPronounList = self.pronounList.copy()
            temporaryEndingsArDefinitePastTenseList = self.endingsArDefinitePastTenseList.copy()
            temporaryEndingsRestDefinitePastTenseList = self.endingsRestDefinitePastTenseList.copy()

            index = random.randint(0, len(temporaryRegularVerbsList) - 1)

            verb = temporaryRegularVerbsList[index]
            stem = verb[0: len(temporaryRegularVerbsList[index]) - 2]
            ending = verb[len(temporaryRegularVerbsList[index]) - 2:]

            if (ending == "AR"):
                self.game3(temporaryPronounList, stem, temporaryEndingsArDefinitePastTenseList, temporaryRegularVerbsList[index])
            elif (ending == "ER" or ending == "IR"):
                self.game3(temporaryPronounList, stem, temporaryEndingsRestDefinitePastTenseList, temporaryRegularVerbsList[index])
            
            del temporaryRegularVerbsList[index]

            if len(temporaryRegularVerbsList) != 0:

                decision = self.prompterBox(title = "Continue?", promptString = "Do you want to continue?" +
                                                "\nType y or Y if yes. Otherwise, type n or N if no.")
                decision = decision.upper()

                if decision == "Y":
                    continue
                elif decision == "N":
                    break

    def conjugationRegularImperfectPast(self):
        self.numberScore = 0
        self.score["text"] = "Score: " + str(self.numberScore)

        temporaryRegularVerbsList = self.regularVerbsList.copy()

        while len(temporaryRegularVerbsList) != 0:
            temporaryPronounList = self.pronounList.copy()
            temporaryEndingsArImperfectPastTenseList = self.endingsArImperfectPastTenseList.copy()
            temporaryEndingsRestImperfectPastTenseList = self.endingsRestImperfectPastTenseList.copy()

            index = random.randint(0, len(temporaryRegularVerbsList) - 1)

            verb = temporaryRegularVerbsList[index]
            stem = verb[0: len(temporaryRegularVerbsList[index]) - 2]
            ending = verb[len(temporaryRegularVerbsList[index]) - 2:]

            self.game3(temporaryPronounList, stem, temporaryEndingsArImperfectPastTenseList, temporaryRegularVerbsList[index])

            if (ending == "AR"):
                self.game3(temporaryPronounList, stem, temporaryEndingsArImperfectPastTenseList, temporaryRegularVerbsList[index])
            elif (ending == "ER" or ending == "IR"):
                self.game3(temporaryPronounList, stem, temporaryEndingsRestImperfectPastTenseList, temporaryRegularVerbsList[index])
            
            del temporaryRegularVerbsList[index]

            if len(temporaryRegularVerbsList) != 0:

                decision = self.prompterBox(title = "Continue?", promptString = "Do you want to continue?" +
                                                "\nType y or Y if yes. Otherwise, type n or N if no.")
                decision = decision.upper()

                if decision == "Y":
                    continue
                elif decision == "N":
                    break
    
    def conjugationRegularFuture(self):
        self.numberScore = 0
        self.score["text"] = "Score: " + str(self.numberScore)

        temporaryRegularVerbsList = self.regularVerbsList.copy()

        while len(temporaryRegularVerbsList) != 0:
            temporaryPronounList = self.pronounList.copy()
            temporaryEndingsFutureTenseList = self.endingsFutureTenseList.copy()

            index = random.randint(0, len(temporaryRegularVerbsList) - 1)

            verb = temporaryRegularVerbsList[index]

            self.game4(temporaryPronounList, temporaryEndingsFutureTenseList, verb)
            
            del temporaryRegularVerbsList[index]

            if len(temporaryRegularVerbsList) != 0:

                decision = self.prompterBox(title = "Continue?", promptString = "Do you want to continue?" +
                                                "\nType y or Y if yes. Otherwise, type n or N if no.")
                decision = decision.upper()

                if decision == "Y":
                    continue
                elif decision == "N":
                    break
    
    def conjugationRegularConditional(self):

        self.numberScore = 0
        self.score["text"] = "Score: " + str(self.numberScore)

        temporaryRegularVerbsList = self.regularVerbsList.copy()

        while len(temporaryRegularVerbsList) != 0:
            temporaryPronounList = self.pronounList.copy()
            temporaryEndingsConditionalTenseList = self.endingsConditionalTenseList.copy()

            index = random.randint(0, len(temporaryRegularVerbsList) - 1)

            verb = temporaryRegularVerbsList[index]

            self.game4(temporaryPronounList, temporaryEndingsConditionalTenseList, verb)
            
            del temporaryRegularVerbsList[index]

            if len(temporaryRegularVerbsList) != 0:

                decision = self.prompterBox(title = "Continue?", promptString = "Do you want to continue?" +
                                                "\nType y or Y if yes. Otherwise, type n or N if no.")
                decision = decision.upper()

                if decision == "Y":
                    continue
                elif decision == "N":
                    break

    def exit(self):
        sys.exit(1)
        
def main():
    print("The program 'Spanish Conjugator' still loading!")
    print("Please wait....")
    SpanishConjugator().mainloop()

if __name__ == "__main__":
    main()