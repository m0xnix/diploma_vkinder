# Дипломная работа

Все слышали про известное приложение для знакомств - Tinder. Приложение предоставляет простой интерфейс для выбора понравившегося человека. Сейчас в Google Play более 100 миллионов установок. 

Используя данные из VK, нужно сделать сервис намного лучше, чем Tinder, а именно: чат-бота “VKinder”. 
Бот должен искать людей, подходящих под условия, на основании информации о пользователе из VK: 
• Возраст, 
• пол, 
• город, 
• семейное положение. 

У тех людей, которые подошли по требованиям пользователю, получать топ-3 популярных фотографии профиля и отправлять их пользователю в чат вместе со ссылкой на найденного человека. Популярность определяется по количеству лайков и комментариев. 

# Входные данные 

• Имя пользователя или его id в ВК, для которого мы ищем пару. если информации недостаточно нужно дополнительно спросить её у пользователя. 

# Требования к сервису: 
1. Код программы удовлетворяет PEP8. 
2. Получать токен от пользователя с нужными правами. 
3. Программа декомпозирована на функции/классы/модули/пакеты. 
4. Результат программы записывать в БД. 
5. Люди не должны повторяться при повторном поиске. 
6. Не запрещается использовать внешние библиотеки для vk. 

# Дополнительные требования (не обязательны для получения диплома): 
1. В vk максимальная выдача при поиске 1000 человек. Подумать как это ограничение можно обойти. 
2. Добавить возможность ставить/убирать лайк, выбранной фотографии.
3. Можно усложнить поиск добавив поиск по интересам. Разбор похожих интересов(группы, книги, музыка, интересы) нужно будет провести с помощью анализа текста. 
4. У каждого критерия поиска должны быть свои веса. То есть совпадение по возрасту должны быть важнее общих групп. Интересы по музыке важнее книг. Наличие общих друзей важнее возраста. И так далее. 
5. Добавлять человека в избранный список, используя БД. 
6. Добавлять человека в черный список чтобы он больше не попадался при поиске, используя БД. 
7. К списку фотографий из аватарок добавлять список фотографий, где отмечен пользователь.
