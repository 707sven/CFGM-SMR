@echo off
TITLE SuperScript

:menu
echo 1. Mostrar los usuarios del sistema
echo 2. Anadir un usuario
echo 3. Cambiar una contrasena de un usuario
echo 4. Eliminar un usuario
echo 5. Efectuar un ping
echo 6. Salir de este Super Script

set /P op=Elige una opcion del menu: 

if %op% == 1 goto:mostrar
if %op% == 2 goto:add
if %op% == 3 goto:cambiar
if %op% == 4 goto:eliminar
if %op% == 5 goto:hacerping
if %op% == 6 goto:salir
echo Elige una opcion que este en el menu.
echo.
pause
cls
goto:menu

:mostrar
net user
echo.
pause
cls
goto:menu

:add
set /P nombredeusuario=Introduce un nombre de usuario: 
net user %nombredeusuario% * /add
echo.
pause
cls
goto:menu

:cambiar
set /P nombredeusuario2=Introduce un nombre de usuario: 
net user %nombredeusuario2% *
echo.
pause
cls
goto:menu

:eliminar
set /P nombreusuario3=Introduce un nombre de usuario: 
net user %nombreusuario3% /delete
echo.
pause
cls
goto:menu

:hacerping
set /P ip=Dame una IP: 
ping %ip%
echo.
pause
cls
goto:menu

:salir
echo Hasta luego.
exit /b