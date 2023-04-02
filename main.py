import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6162555392:AAEI8VyAbQZSKDOMDHaDk3ulIBGtg8l_9aU'

openai.api_key = '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'

Bot = Bot(token)
dp = Dispatcher(Bot)

@dp.message_handler()
async def send(message : types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
    )

    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)





