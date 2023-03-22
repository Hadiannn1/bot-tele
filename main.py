import openai
from aiogram import Bot, Dispatcher, types, executor

token = '<ISI DENGAN TOKEN BOTFATHER>'
openai.api_key= '<ISI DENGAN API DARI OPEN.AI>'

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
