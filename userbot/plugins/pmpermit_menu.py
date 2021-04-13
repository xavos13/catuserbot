"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
Credits: written by ༺αиυвιѕ༻ {@A_Dark_Princ3}
"""
import asyncio

from telethon import events, functions

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql

from . import ALIVE_NAME, PM_START, PMMESSAGE_CACHE, set_key

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
PREV_REPLY_MESSAGE = {}
PM = f"""Olá. Você está acessando o menu disponível do meu mestre, {DEFAULTUSER}.
__Vamos deixar isso tranquilo e me dizer por que você está aqui.__
**Escolha um dos seguintes motivos pelos quais você está aqui:**

`a`. Para conversar com meu mestre
`b`. Para spam na caixa de entrada do meu mestre.
`c`. Para perguntar algo
`d`. Para pedir algo\n"""
ONE = """__OK. Sua solicitação foi registrada. Não envie spam para a caixa de entrada do meu mestre. Você pode esperar uma resposta nos próximos anos. Ele / Ela é um homem ocupado, ao contrário de você provavelmente.__

**⚠️ Você será bloqueado e denunciado se enviar spam. ⚠️**\n\n"""
TWO = " `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\n**Tão chato, esta não é sua casa. Vá incomodar outra pessoa. Você foi bloqueado e denunciado até novo aviso.**"
THREE = "__OK. Meu mestre ainda não viu sua mensagem.Ele / Ela geralmente responde às pessoas, embora se preocupe com as que já partiram.__\n __Ele responderá quando voltar, se quiser. Já há muitas mensagens pendentes😶__\n **Não envie spam, a menos que deseje ser bloqueado e denunciado.**"
FOUR = "`OK. por favor, tenha as maneiras básicas de não incomodar muito meu mestre. Se ele / ela deseja ajudá-lo, ele / ela responderá a você em breve.`\n**Não pergunte repetidamente, senão você será bloqueado e denunciado.**"
LWARN = "**Este é o seu último aviso. NÃO envie outra mensagem, senão você será bloqueado e denunciado. Mantenha a paciência. Meu mestre irá responder o mais rápido possível.**\n"


@bot.on(events.NewMessage(pattern=r"\/start", incoming=True))
async def _(event):
    if event.fwd_from:
        return
    chat_id = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if chat_id not in PM_START:
            PM_START.append(chat_id)
        if not event.is_private:
            return
        set_key(PMMESSAGE_CACHE, event.chat_id, event.id)
        try:
            async with event.client.conversation(chat) as conv:
                if pmpermit_sql.is_approved(chat_id):
                    return
                test1 = await event.client.send_message(chat, PM)
                set_key(PMMESSAGE_CACHE, event.chat_id, test1.id)
                chat_id = event.sender_id
                response = await conv.get_response(chat)
                y = response.text
                if y == "a" or "A":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test2 = await event.client.send_message(chat, ONE)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test2.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test3 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test3.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test4 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test4.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "b" or "B":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test5 = await event.client.send_message(chat, LWARN)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test5.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test6 = await event.client.send_message(chat, TWO)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test6.id)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "c" or "C":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test7 = await event.client.send_message(chat, THREE)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test7.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test8 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test8.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test9 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test9.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "d" or "D":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test10 = await event.client.send_message(chat, FOUR)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test10.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test11 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test11.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            await event.client.send_message(chat, TWO)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                else:
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    test12 = await event.client.send_message(
                        chat,
                        "You have entered an invalid command. Please send `/start` again or do not send another message if you do not wish to be blocked and reported.",
                    )
                    set_key(PMMESSAGE_CACHE, event.chat_id, test12.id)
                    response = await conv.get_response(chat)
                    z = response.text
                    if z != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test13 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test13.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test14 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test14.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
        except Exception as e:
            LOGS.info(str(e))
