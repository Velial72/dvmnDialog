import random

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from environs import Env

from dialog import detect_intent_text


env = Env()
env.read_env()

VK_TOKEN = env('VK_TOKEN')


def send_answer(answer, user_id, vk_api):
    vk_api.messages.send(
        user_id=user_id,
        message=answer,
        random_id=random.randint(1,1000)
    )


if __name__ == "__main__":
    VK_TOKEN = env('VK_TOKEN')
    vk_session = vk.VkApi(token=VK_TOKEN)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            serialized_answer = detect_intent_text('dvmn-bot-ynkq', event.user_id, event.text, flag=True)
            if serialized_answer is not None:
                send_answer(serialized_answer['answer'], event.user_id, vk_api)
