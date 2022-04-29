# Battery Notification in Audio using Fish Shell

Some desktop environments provide battery notification so that every time battery is low or maybe full, the DE will notify us. The notification usually comes as something like tooltip which may not be handy if we are not in front of our monitor or maybe still concentrate on our tasks. Also, sometimes I want to change my DE or window manager - KDE to GNOME, AwesomeWM to Spectrwm, etc. In this situation I usually stuck. [Conky](https://github.com/brndnmtthws/conky) can help but changing WM / DE involves struggling with configuration file(s) and/or more software (panel, for example).

So, that was my problem. I want to have a very simple and can be used to notify my battery status. I decide to use audio to notify myself since it can be used across any DE/WM. All I need to do is just prepare two audio files (you can create that by yourself or download from the Internet) and create this script:

```bash
#!/usr/bin/fish

set bcapacity (cat /sys/class/power_supply/BAT0/capacity)
set bstatus (cat /sys/class/power_supply/BAT0/status)

if [ "$bcapacity" -le 15 -a "$bstatus" = "Discharging" ]
  /usr/bin/mpg123 /home/bpdp/Musik/battlow.mp3
end

if [ "$bcapacity" -gt 90 -a "$bstatus" = "Charging" ]
  /usr/bin/mpg123 /home/bpdp/Musik/battfull.mp3
end
```

Let's say, I put that file in `$HOME/bin/batt.sh`. I install [mpg123](https://www.mpg123.de/) for my player and put those `mp3` files at `/home/bpdp/Musik/battlow.mp3` for battery low audio and `/home/bpdp/Musik/battfull.mp3` for battery full audio.

Put the script into a crontab by `crontab -e` and write then save this:

```bash
*/2 * * * * /home/bpdp/bin/batt.sh
```

so that every 2 minutes,my battery will be checked. Run cron daemon (I use `OpenRC`, might be different if you use `systemd`):

```
sudo rc-service cron start
```

That's all. 
