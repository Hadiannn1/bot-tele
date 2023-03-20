# Telegram Bot OpenAI ChatGPT version Python by Wannazid
import openai
from aiogram import Bot, Dispatcher, types, executor

bot_tkn = '6279616551:AAGQxe5VII1x1bRGkOlJ7-3BOrV5i3QV7Ss'
openai.api_key= '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'

bot = Bot(token=bot_tkn)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start','help'])
async def user_come(pesan: types.Message):
	await pesan.answer('Selamat Datang, takuni napa aja')
	
@dp.message_handler(lambda message: message.text)
async def ai_answer(message: types.Message):
	respon = openai.Completion.create(model='text-davinci-003', prompt=message.text, temperature=0, max_tokens=1000)
	parse = respon['choices'][0]['text']
	await message.reply(parse)
	
print('Bot begawi')	
executor.start_polling(dp)