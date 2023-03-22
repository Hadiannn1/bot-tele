import openai
from aiogram import Bot, Dispatcher, types, executor

token = '6279616551:AAGQxe5VII1x1bRGkOlJ7-3BOrV5i3QV7Ss'
openai.api_key= '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'

bot = Bot(token=token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def user_come(message: types.Message):
	await message.answer('Hai, Silahkan tanyakan apa saja')

@dp.message_handler(lambda message: message.text)
async def ai_answer(message: types.Message):
	respon = openai.Completion.create(model='text-davinci-003', prompt=message.text, temperature=1, max_tokens=1000)
	parse = respon['choices'][0]['text']
	await message.reply(parse)
	
print('Bot Running')	
executor.start_polling(dp)
