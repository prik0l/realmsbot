import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


bot = Bot(token="1650340335:AAHnoP_Dbdz7Y3ysAVJIYtz9PDVzHC_MOLA")
dp = Dispatcher(bot, storage=MemoryStorage())

# Каким чатам разрешить взаимодействия с ботом?
allow_chats = ['121020442', '-1001450184674', '-1001292573675']
# Сообщение если чат не разрешен
group_error_msg = "Я работаю только в группе;)"
# Ссылка на сервер
realms_link = "https://realms.gg/YPuzb--bMDE"


# Заготовки для трёх предложений
first = ["На сегодняшний день, выдача паспортов осуществляется в городе УТМ в здании паспортного стола.\n У здания паспортного стола стоит кафедра, в которой выписан перечень вещей, необходимых для получения паспорта...\n\n Паспорт- это основной документ, удостоверяющий личность гражданина.\n Паспорт не ограничен в сроке действия и подразумевает возможно смены паспорта с определенными причинами:\n\n • Смена города проживания;\n • Смена имени или фамилия;\n • Утеря паспорта и т.д...\n\n В зависимости от причины смены паспорта, изменяется и цена на его изготовления. \n Самый первый паспорт стоит 2 АР, если вы желаете сменить имя или фамилия или другая обычная причина, то с вас возьмут те же 2 АР, но если вы потеряли, испортили, утилизировали паспорт, с вас возьмут уже 5 АР, поэтому будьте аккуратны с документом.\n\n Помимо 2 АР вы должны будете сдать 3 книги: \n\n • Книга №1\n В этой книге вы пишете свой игровой ник, вымышленные имя и фамилию, город проживания и род вашей деятельности (фермер, маг, торговец и т.д);\n\n • Книга №2 и №3 остаются пустые и предназначены для того, чтобы служить паспортом и копией паспорта.\n\n Всё это вы можете собрать в шалкер, при возможности, или же просто сложить максимально близко к друг другу в сундуке, стоящем в паспортном столе. После того, как вы сдали всё необходимое, работник паспортного стола займётся изготовлением вашего документа и в скором времени оповестит вас о его готовности.\n\n По другим вопросам, связанными с паспортом и его изготовлением обращайтесь в группу или к действующему работнику структуры."]
second = ["Система налогов:\n Каждые 7 дней вы должны выплатить налоги, в размере 1АР с человека, и 1АР за каждый бизнес, в казну своего города.\n Новички освобождены от оплаты на неделю.\n Выплатить налоги можно в течении 4 дней.\n На 5 день Вам прийдёт предупреждение о неоплате (письмо в почтовый ящик.\n На 6 день Вам будет выписан штраф в размере 1АР.\n В случае злостной неуплаты, мы будем вынуждены подать на Вас в суд!\n С уважением, налоговая сервера!"]
third = ["Основные правила сервера:\n<==============>\n[1] За что вам могут дать бан?\n•Гриф\n•Воровсто\n•Читы\n•Баги которые облегчают игру\n•Аддоны которые влияют на игру\n•Использование невидимых скинов.\n<==============>\n[2] За что вам могут выдать штраф:\n•Вход на запрещённую тереториию (помечено табличкой).\n•Взрыв крипера на чей-то теретории.\n•Разрушение чужих построек<==============>\n[3] Дополнение:\nТаблички:\n Если вы видите табличку с надписью вход запрещен, то значит что вход ЗАПРЕЩЕН, и вам там делать нечего, вход для вас закрыт, и не важно вы только посмотреть или вам туда нужно, вам туда НЕЛЬЗЯ.\n\nЕсли вы нашли блок/другой рес, и он вам не принадлежит - не трогайте его, это не ваше, тот кто оставил/забыл, прийдет и заберёт, поставтие себя на место того , кто этот рес забыл, приходите а его кто то украл, не очень да?\nВывод: не ваше - не трогайте\n\nТаже самая история с животными например лошадь, вот стоит лошадь в броне чья-то, вам её трогать/кататься на ней - нечего, она не ваша!\n\nУВАЖАЙТЕ ДРУГ ДРУГА"]
valutamsg = ["ВАЛЮТА\nАР\n(Алмазная руда)\nДобывается шёлком\n\nУ вас нет шёлка?\n\nСпрашивайте кому нужна помощь, и работайте у них, за зарплату договаривайтесь заранее, за ары вы можете купить вещи или получить какую-либо услугу."]
none = [""]
red = ["Увы.\nВыпал, красный 🔴️\nТы получаешь бан."]
black = ["Увы.\nВыпал, черный ⚫️\nТы получаешь бан."]


logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())