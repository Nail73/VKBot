from vkbottle.bot import Bot, Message
from config import token
from vkbottle.dispatch.rules import ABCRule
from loguru import logger


class AdminRule(ABCRule[Message]):
    def __init__(self, admins: list):
        self.admins = admins

    async def check(self, event: Message):
        return event.from_id in self.admins


logger.disaible('vkbottle')
bot = Bot(token = token)
bot.labeler.custom_rules['is_admin'] = AdminRule



@bot.on.message(attachment = 'photo')
async def photo_answer(message: Message):
    await message.answer('Спасибо за фото. Принял.')

@bot.on.message(id_admin = 'my_id')
async def admin_exe(message: Message):
    await message.answer(f'Админ написал: <{message.text}>')


@bot.on.message()
async def main(message: Message):
    await message.answer(f'Пользователь написал: <{message.text}>')

bot.run_forever()