import openai
from aiogram import Bot, Dispatcher, types, executor

tk = '6279616551:AAGQxe5VII1x1bRGkOlJ7-3BOrV5i3QV7Ss'
openai.api_key= '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'

bot = Bot(token=tk)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def user_come(message: types.Message):
	await message.answer('Silahkan tanyakan apa saja')

@dp.message_handler(commands=['help'])
async def user_come(message: types.Message):
	await message.answer('Jika butuh bantuan hubungi @nyumiXDii')

@dp.message_handler(commands=['donate'])
async def user_come(message: types.Message):
    await message.answer('silahkan donasi ke https://sht.moe/oeABa')

@dp.message_handler(lambda message: message.text)
async def ai_answer(message: types.Message):
	respon = openai.Completion.create(model='text-davinci-003', prompt=message.text, temperature=1, max_tokens=1000)
	parse = respon['choices'][0]['text']
	await message.reply(parse)
	
print('Bot Running @nyumichatbot')	
executor.start_polling(dp)