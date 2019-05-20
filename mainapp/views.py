
from django.shortcuts import render
import time
import json
import base64
import io
from django.http import HttpResponse
import optidrill.neuralmodels as NM

#import HotsNeural.neuralmodels as NM
from pprint import pprint



def home(request):
    return render(request, 'index.html')

def analyzeGeoProg(request):
    if request.method=="POST":
        FormData = request.POST
        tableJSON = FormData.get("tableJSON","")
        tableJSON = json.loads(tableJSON)

        stuckProb = []
        for row in tableJSON:

            Formation = row["FormationName"]
            MinWeight = float(row["MinWeight"])
            MaxWeight = float(row["MaxWeight"])
            Caudal = float(row["Caudal"])
            MDTope = float(row["MDTope"])
            MDBase = float(row["MDBase"])

            
            if Formation=='Formacion 11':
                FormationOHE = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
            elif Formation=='Formacion 16':
                FormationOHE = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
            elif Formation=='Formacion 7':
                FormationOHE = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
            elif Formation=='Formacion 3':
                FormationOHE = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
            elif Formation=='Formacion 12':
                FormationOHE = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
            elif Formation=='Formacion 14':
                FormationOHE = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
            elif Formation=='Formacion 6':
                FormationOHE = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
            elif Formation=='Formacion 4':
                FormationOHE = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
            elif Formation=='Formacion 9':
                FormationOHE = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
            elif Formation=='Formacion 2':
                FormationOHE = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
            elif Formation=='Formacion 5':
                FormationOHE = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
            elif Formation=='Formacion 10':
                FormationOHE = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            elif Formation=='Formacion 13':
                FormationOHE = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
            elif Formation=='Formacion 8':
                FormationOHE = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
            elif Formation=='Formacion 15':
                FormationOHE = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
            else:
                FormationOHE = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


            stuck = NM.getStuckProb(FormationOHE,MinWeight,MaxWeight,Caudal,MDTope,MDBase)

            print(stuck)

            stuckDict = [Formation, float(round(stuck[0][0]*100,2))]
            stuckProb.append(stuckDict)



        return render(request, 'analysisresult.html',dict(stuckProb=stuckProb))