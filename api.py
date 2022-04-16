from flask import Flask
import requests
import json


print()
app = Flask(__name__)

@app.route('/')
def home():
    return 'seu ip foi logged'

@app.route('/info=<dado>')
def dados(dado):
    emailsenha = dado.split(':')
    jso = {
    "login": emailsenha[0],
    "password": emailsenha[1],
    }
    


    token = requests.post('https://discord.com/api/v9/auth/login',json=jso).text

    if not 'token' in token:
        return '{"status": invalid}, login invalido'
    else:


        dados = json.loads(token)

        user_token = dados['token']

        hea = {
            'authorization': user_token
        }

        infoz = requests.get('https://discordapp.com/api/v9/users/@me',headers=hea)
  
        info = json.loads(infoz.text)

        id = info['id']
        public_flags = info['public_flags']


        flags = {
            131072: ['DEVELOPPER'],
            65536: ['VERIFIED_BOT'],
            16384: ['BUG_HUNTER_LEVEL_2'],
            4096: ['SYSTEM'],
            1024: ['TEAM_USER'],
            512: ['PIG'],
            256: ['HYPESQUAD3'],
            128: ['HYPESQUAD2'],
            64: ['HYPESQUAD1'],
            8: ['BUG_HUNTER_LEVEL_1'],
            4: ['HYPESQUAD'],
            2: ['PARTNER'],
            1: ['STAFF']
        }

        things = []

        while public_flags != 0:
            for item in flags.keys():
                if public_flags >= item:
                    things.append(flags[item][0])
                    public_flags = public_flags - item






        
        info2 = requests.get(f'https://discord.com/api/v9/users/{id}/profile?with_mutual_guilds=false',headers=hea).text
     

        infu = json.loads(info2)

        boost = infu['premium_guild_since']
        classic = infu['premium_since']

        user_boost = 'nao'
        user_classic = 'nao'

        try:
            if not 'ull' in boost:
                user_boost = 'sim'
            if not 'ull' in classic:
                user_classic = 'sim'
        except:
            user_classic = 'nao'
            user_boost = 'nao'



        retorno = {
            'token':user_token,
            'id':info['id'],
            'nick':info['username'],
            'tag':info['discriminator'],
            'bio':info['bio'],
            'local':info['locale'],
            'mfa':info['mfa_enabled'],
            'email':info['email'],
            'telefone':info['phone'],
            'verificado':info['verified'],
            'nitro_boost':user_boost,
            'nitro_classic':user_classic,
            'badges':things
        }

        return retorno

app.run()