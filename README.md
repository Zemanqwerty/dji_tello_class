# dji_tello_class

---

для начала создаём виртуальное окружение и ставим все нужные библиотеки

   pip install -r requirements.txt
   
---
Необходимо создать в основной директории папку media, в неё будут сохраняться снятые фото и видео.

Для работы используем файл app.py. В нём осуществляется работа с коптером. В данный файл
уже импортирован класс-обработчик для работы с коптером, поэтому вся работа будет осуществляться через него.

Работа с камерой осуществляется напрямую в классе. Пример "drone.make_picture()"
Работа с управлением осуществляется через вложенный класс drone. пример "drone.drone.takeoff()"

Скрипт должен заканчиваться отсоединением от дрона "drone.drone.end()"


