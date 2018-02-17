import requests
import twitter
import time
import random
from urllib.parse import urlencode, quote_plus

# Parametros #
INTERVALO = 600
HILO_ACTUAL="32124"
HEADER = "[i]Chispa bot v0.1.5[/i]\n\n"
###

unicos = set()
q1 = {'l':'es',
            'q': '#6Ago from:FreddyGuevaraC OR from:ElyangelicaNews OR from:AlbertoRT51 OR from:puzkas OR from:victoramaya OR from:AndrewsAbreu OR from:PeriodistaDSD OR from:ismaelgabriel22 OR from:_humanoderecho OR from:NituPerez OR from:MelanioBar OR from:PeriodistaDSD OR from:DSDVenezuela OR from:Juliococo OR from:MPvenezolano',
            'result_type':'recent',
            'tweet_mode':'extended'}

q2 = {'l':'es',
            'q': 'URGENTE OR urgente OR ULTIMO OR MOMENTO OR ultimo OR momento OR muerto OR asesinado OR bala OR balas OR mortero OR explosion OR sanciones OR lista -servicio -publico -medicamentos -medicamento -#ServicioPúblico #6Ago',
            'result_type':'recent',
            'tweet_mode':'extended'}

query1 = urlencode(q1, quote_via=quote_plus)
query2 = urlencode(q2, quote_via=quote_plus)

api = twitter.Api(consumer_key='0FJB',
                      consumer_secret='OTp',
                      access_token_key='1W',
                      access_token_secret='4b')

class tuit:
    def __init__(self, usuario, texto, link):
        self.usuario = usuario
        self.texto = texto
        self.link = link

    def __eq__(self, other):
        return self.texto == other.texto

    def __hash__(self):
        return hash(self.texto)

    def __str__(self):
        return self.link+"\n[b]@"+self.usuario+"[/b]: "+ (str(self.texto).replace(" q ","que"))

def postear(texto, hilo):
    print("Posteando en /ve/"+hilo)
    r = requests.post("https://www.hispachan.org/board.php",
    data={
        "board":"ve",
        "replythread":hilo,
        "MAX_FILE_SIZE":"12582912",
        "email":"",
        "subject":"",
        "em":"OP",
        "message":texto,
        "postpassword":"N1rJH6LN"
    })

def buscarYPostear():
    global unicos
    tweets = api.GetSearch(raw_query=query1)
    posteo = HEADER
    
    for t in tweets:
        unicos.add(tuit(t.user.screen_name, t.full_text, "https://twitter.com/statuses/"+str(t.id)))
 
    tweets = api.GetSearch(raw_query=query2)

    for t in tweets:
        unicos.add(tuit(t.user.screen_name, t.full_text, "https://twitter.com/statuses/"+str(t.id)))

    for t in random.sample(unicos, 5):
        posteo += str(t) +"\n\n"
    
    postear(posteo, HILO_ACTUAL)
    print(posteo)
    unicos = set()
   

def inicio():
    while True:
        buscarYPostear()
        time.sleep(INTERVALO)

inicio()
