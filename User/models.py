from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class Newuser(AbstractUser):
    health = models.IntegerField("HP",default=100)
    attack = models.IntegerField("ATTACK",default=5)
    defence = models.IntegerField("ARMOR",default=3)
    img = models.ImageField("IMG",upload_to="img/",default="")
    balance = models.DecimalField("MONEY", default=100, decimal_places=0,max_digits=10)
    lvl = models.IntegerField("LEVEL",default=1)
    exp = models.IntegerField("EXP",default=0)
    weapon = models.ForeignKey('Weapon',verbose_name="WEAPON",default='',null=True,blank=True,on_delete=models.SET_NULL)
    armor = models.ForeignKey('Armor',verbose_name="ARMOR",default='',null=True,blank=True,on_delete=models.SET_NULL)
    dungeon_lvl = models.IntegerField("DUNGEON LVL",default=1)
    dungeon_loc = models.IntegerField("DUNGEON LOCATION", default=0)
    is_fight = models.BooleanField("IS FIGHT",default=False)
    enemy = models.ForeignKey("Enemy",verbose_name="ENEMY",default='',null=True,blank=True,on_delete=models.SET_NULL)

    def ReturnAllDamage(self):
        if self.weapon is None:
            return self.attack
        else:
            return self.attack+self.weapon.damage

    def ReturnAllArmor(self):
        if self.armor is None:
            return self.defence
        else:
            return self.defence+self.armor.armor

    def CheckEXP(self):
        if self.lvl >= 99:
            self.lvl=99
            self.exp=99
        else:
            if self.exp>=100:
                self.lvl+=1
                self.defence=self.defence+1
                self.attack=self.attack+1
                self.exp=0
        self.save()
        return self.lvl

    def get_absolute_url(self):
        return reverse("del", kwargs={"pk": self.pk})

    def get_absolute_url_upd(self):
        return reverse("upd", kwargs={"pk": self.pk})
    
    def get_absolute_url_sleep(self):
        return reverse("sleeping", kwargs={"pk": self.pk})
    
    def get_absolute_url_fight(self):
        return reverse("fight", kwargs={"pk": self.pk})

    def get_absolute_url_bossfight(self):
        return reverse("bossfight", kwargs={"pk": self.pk})

    def get_absolute_url_bossfight_st(self):
        return reverse("bossfight_st", kwargs={"pk": self.pk})

    def get_absolute_url_urs(self):
        return reverse("user", kwargs={"pk": self.pk})

    def __str__(self):
        return self.username

class Weapon(models.Model):
    name = models.CharField("WEAPON NAME",max_length=30)
    damage = models.IntegerField("DAMAGE+")
    img = models.ImageField("IMG",upload_to="weapon")
    balance = models.IntegerField("SUM")
    lvl = models.IntegerField("LVL")
    dun_lvl = models.IntegerField("DUNGEON LVL")

    def get_absolute_url(self):
        return reverse("buy_w", kwargs={"weapon": self.pk})
    

    def __str__(self):
        return self.name
    

class Armor(models.Model):
    name = models.CharField("ARMOR NAME",max_length=30)
    img = models.ImageField("IMG",upload_to="armor")
    armor = models.IntegerField("AROMOR+")
    balance = models.IntegerField("SUM")
    lvl = models.IntegerField("LVL")
    dun_lvl = models.IntegerField("DUNGEON LVL")

    def get_absolute_url(self):
        return reverse("buy_a", kwargs={"armor": self.pk})

    def __str__(self):
        return self.name

class Enemy(models.Model):
    name = models.CharField("NAME",max_length=40)
    health = models.IntegerField("HP",default=100)
    attack = models.IntegerField("ATTACK",default=1)
    defence = models.IntegerField("ARMOR",default=1)
    lvl = models.IntegerField("LEVEL",default=1)
    slug = models.SlugField("URL",unique=True)
    img = models.ImageField("IMG",upload_to="enemy/",default="")

    weapon = models.ForeignKey('Weapon',verbose_name="WEAPON",default=None,null=True,blank=True,on_delete=models.SET_NULL)
    armor = models.ForeignKey('Armor',verbose_name="ARMOR",default=None,null=True,blank=True,on_delete=models.SET_NULL)

    def ReturnAllDamage(self):
        if self.weapon is None:
            return self.attack
        else:
            return self.attack+self.weapon.damage

    def ReturnAllArmor(self):
        if self.armor is None:
            return self.defence
        else:
            return self.defence+self.armor.armor