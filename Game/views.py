from django.shortcuts import redirect,render
from django.template.loader import render_to_string
from django.views.generic import TemplateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
import random
from django.http import JsonResponse
from Game.forms import AttackF
from User.models import Armor, Enemy, Newuser, Weapon

class Location1(LoginRequiredMixin,TemplateView):
    template_name='BK/home.html'

class Location2(LoginRequiredMixin,TemplateView):
    template_name='BK/loc_2.html'

class SleepRoom(LoginRequiredMixin,TemplateView):
    template_name='BK/sleep.html'

class Sleepes(LoginRequiredMixin,TemplateView):
    template_name="BK/sleep_mes.html"

def Sleeping(request,pk):
    user = Newuser.objects.get(pk=pk)
    if request.user.pk == user.pk:
        if user.health == 100:
            return redirect('sleep')
        else:
            if user.balance < 30:
                return redirect('sleep')
            else:
                user.balance -= 30
                user.health = 100
                user.save()
        return redirect('sleeped')
    else:
        return redirect('sleep')
    
class Location3(LoginRequiredMixin, TemplateView):
    template_name="BK/loc_3.html"

class Shop(LoginRequiredMixin, TemplateView):
    template_name="BK/shop.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["weapons"] = Weapon.objects.all()
        context['armors'] = Armor.objects.all()
        return context

def buyweapon(request,weapon):
    weapon = Weapon.objects.get(pk=weapon)
    user = request.user
    if user.balance>=weapon.balance:
        if user.weapon==weapon:
            return render(request,'BK/shop_err.html')
        else:
            if weapon.lvl<=request.user.lvl:
                user.balance -= weapon.balance
                user.weapon = weapon
                user.save()
            else:
                return render(request,'BK/shop_mes.html')

    else:
        return render(request,'BK/shop_err.html')
    return redirect('success_b')

def buyarmor(request,armor):
    armor = Armor.objects.get(pk=armor)
    user = request.user
    if user.balance>=armor.balance:
        if user.armor==armor:
            return render(request,'BK/shop_err.html')
        else:
            if armor.lvl<=request.user.lvl:
                user.balance -= armor.balance
                user.armor = armor
                user.save()
            else:
                return render(request,'BK/shop_mes.html')
    else:
        return render(request,'BK/shop_err.html')
    return redirect('success_b')

class SuccesBuy(LoginRequiredMixin,TemplateView):
    template_name='BK/success_buy.html'

class Location4(LoginRequiredMixin,TemplateView):
    template_name='BK/loc_4.html'

class Dungeon(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        if request.user.dungeon_loc == 3 or request.user.is_fight:
            request.user.health = 0
            request.user.dungeon_loc = 0
            request.user.is_fight = 0
            request.user.save()
            if request.user.enemy is not None:    
                enemy = Enemy.objects.get(slug=request.user.username)
                enemy.delete()
            return render(request,'BK/dungeon.html')
        else:
            return render(request,'BK/dungeon.html')

class DungeonGo(LoginRequiredMixin,View):

    def get(self,request,*args, **kwargs):
        if request.user.dungeon_loc == 3 or request.user.is_fight:
            request.user.health = 0
            request.user.dungeon_loc = 0
            request.user.is_fight = False
            request.user.save()
            if request.user.enemy is not None:    
                enemy = Enemy.objects.get(slug=request.user.username)
                enemy.delete()
        if request.user.health<10:
            return render(request,'BK/enter_err.html')
        select = random.randint(1,100)
        if select<=30:
            request.user.dungeon_loc = 1
            request.user.save()
            return redirect('dun_loc1')
        elif select>30 and select<=50:
            request.user.dungeon_loc = 2
            request.user.save()
            return redirect('dun_loc2')
        elif select>50 and select<=75:
            request.user.dungeon_loc = 4
            request.user.save()
            return redirect('dun_loc4')
        elif select>75 and select<=100:
            request.user.dungeon_loc = 3
            request.user.save()
            return redirect('dun_loc3')

class Dungeon_Loc1(LoginRequiredMixin,View):

    def get(self,request,*args, **kwargs):
        if request.user.dungeon_loc == 3:
            request.user.health = 0
            request.user.dungeon_loc = 0
            request.user.is_fight = False
            request.user.save()
            if request.user.enemy is not None:    
                enemy = Enemy.objects.get(slug=request.user.username)
                enemy.delete()    
        if self.request.user.dungeon_loc == 1:
            return render(request,'BK/dun1.html')
        else:
            self.request.user.dungeon_loc = 0
            self.request.user.save()
            return redirect('dungeon')


class Dungeon_Loc4(LoginRequiredMixin,View):

    def get(self,request,*args, **kwargs):
        if request.user.dungeon_loc == 3:
            request.user.health = 0
            request.user.dungeon_loc = 0
            request.user.is_fight = False
            request.user.save()
            if request.user.enemy is not None:    
                enemy = Enemy.objects.get(slug=request.user.username)
                enemy.delete()    
        if self.request.user.dungeon_loc == 4:
            return render(request,'BK/dun4.html')
        else:
            self.request.user.dungeon_loc = 0
            self.request.user.save()
            return redirect('dungeon')

class Healing(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        if request.user.health >= 100:
            return render(request,'BK/heal_err.html')
        else:
            if request.user.balance>=5:
                request.user.balance-=5
                request.user.health += 30
                if request.user.health > 100:
                    request.user.health = 100
                request.user.save()
                return render(request,'BK/success_heal.html')
            else:
                return render(request,'BK/heal_err.html')

class Dungeon_Loc2(LoginRequiredMixin,View):
    
    def get(self,request,*args, **kwargs):   
        if request.user.dungeon_loc == 3:
            request.user.health = 0
            request.user.dungeon_loc = 0
            request.user.is_fight = False
            request.user.save() 
            if request.user.enemy is not None:    
                enemy = Enemy.objects.get(slug=request.user.username)
                enemy.delete()
        if self.request.user.dungeon_loc == 2:
            return render(request,'BK/dun2.html')
        else:
            self.request.user.dungeon_loc = 0
            self.request.user.save()
            return redirect('dungeon')


class Dungeon_Loc3(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):    
        if self.request.user.dungeon_loc == 3:
            return render(request,'BK/dun3.html')
        else:
            self.request.user.dungeon_loc = 0
            self.request.user.save()
            return redirect('dungeon')

class PayBadGuys(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        if request.user.dungeon_lvl == 1:
            pay = random.randint(50,100)
        elif request.user.dungeon_lvl == 2:
            pay = random.randint(80,150)
        elif request.user.dungeon_lvl == 3:
            pay = random.randint(200,400)
        if self.request.user.balance>=pay:    
            self.request.user.balance -= pay
            self.request.user.dungeon_loc = 0
            self.request.user.save()
        else:
            return render(request,'BK/pay_err.html',context={'price':pay}) 
        return render(request,'BK/payed.html',context={'price':pay})    

class TakeTreasure(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        if request.user.dungeon_loc == 2:
            pay = 0
            damage = random.randint(0,15)
            if request.user.dungeon_lvl == 1:
                pay = random.randint(50,100)
            elif request.user.dungeon_lvl == 2:
                pay = random.randint(100,200)
            elif request.user.dungeon_lvl == 3:
                pay = random.randint(300,500)
            request.user.balance += pay
            request.user.exp += random.randint(1,5)
            request.user.dungeon_loc = 0
            if damage - (int(request.user.ReturnAllArmor()/2)) >= 0:
                request.user.health -= damage - (int(request.user.ReturnAllArmor()/2))
            request.user.save()
            return render(request,'BK/success_take.html',context={'price':pay})
        else:
            return redirect('dungeon')

class Fight(LoginRequiredMixin,UserPassesTestMixin,View):

    def get(self,request,*args, **kwargs):
        form_class = AttackF()
        if request.user.is_fight==False:
            request.user.is_fight = True
            allphoto = ['enemy/first.jpg','enemy/second.jpg']
            rnd = random.randint(0,1)
            if request.user.dungeon_lvl == 1:
                enemy = Enemy.objects.create(name="Bad_Guy_lvl_1",attack=5,defence=2,lvl=1,img=allphoto[rnd],slug=request.user.username)
            elif request.user.dungeon_lvl == 2:
                enemy = Enemy.objects.create(name="Bad_Guy_lvl_2",attack=10,defence=8,lvl=2,img=allphoto[rnd],slug=request.user.username,weapon=Weapon.objects.get(pk=2),armor=Armor.objects.get(pk=2))
            elif request.user.dungeon_lvl == 3:
                enemy = Enemy.objects.create(name="Bad_Guy_lvl_3",attack=30,defence=25,lvl=3,img=allphoto[rnd],slug=request.user.username,weapon=Weapon.objects.get(pk=4),armor=Armor.objects.get(pk=4))
            elif request.user.dungeon_lvl == 4:
                enemy = Enemy.objects.create(name="Bad_Guy_lvl_4",attack=40,defence=35,lvl=4,img=allphoto[rnd],slug=request.user.username,weapon=Weapon.objects.get(pk=5),armor=Armor.objects.get(pk=5))
            request.user.enemy = enemy
            request.user.save()
            return render(request,'BK/fight.html',context={'enemy':enemy,'form':form_class})
        else:
            enemy = Enemy.objects.get(slug=request.user.username)
            return render(request,'BK/fight.html',context={'enemy':enemy,'form':form_class})
    
    def post(self,request,*args, **kwargs):
        form_class = AttackF(request.POST)
        enemy = Enemy.objects.get(slug=request.user.username)
        choic = {0:'head',1:'body',2:'legs'}
        selat = random.randint(0,2)
        seldef = random.randint(0,2)
        if request.POST['attack'] == choic[seldef]:
            msg_enemy_def = "Enemy blocked your atack!"
            msg_at = ""
        else:
            if request.user.ReturnAllDamage() - (int(enemy.ReturnAllArmor()/2))>=0:    
                enemy.health -= request.user.ReturnAllDamage() - (int(enemy.ReturnAllArmor()/2))
                enemy.save()
                msg_enemy_def = ""
                msg_at = f"Your atack ({request.POST['attack']}) is success (-{request.user.ReturnAllDamage() - (int(enemy.ReturnAllArmor()/2))})"
            else:
                msg_enemy_def = ""
                msg_at = f"Your atack ({request.POST['attack']}) is success (0)"
        if request.POST['defence'] == choic[selat]:
            msg_def = "You blocked enemy atack!"
            msg_enemy_at = ""
        else:
            if enemy.ReturnAllDamage() - (int(request.user.ReturnAllArmor()/2))>=0:
                request.user.health -= enemy.ReturnAllDamage() - (int(request.user.ReturnAllArmor()/2))
                request.user.save()
                msg_def = ""
                msg_enemy_at = f"Enemy atack ({choic[selat]}) is success (-{enemy.ReturnAllDamage() - (int(request.user.ReturnAllArmor()/2))})"
            else:
                msg_def = ""
                msg_enemy_at = f"Enemy atack ({choic[selat]}) is success (0)"
        if request.user.health <= 0:
            request.user.health = 0
            request.user.dungeon_loc = 0
            request.user.is_fight = False
            self.request.user.save()
            enemy.delete()
            html = render_to_string(request=request,template_name='BK/lose.html')
            return JsonResponse({"html":html},status=200)
        elif enemy.health <= 0:
            request.user.is_fight = False
            request.user.dungeon_loc = 0
            request.user.exp += random.randint(15,30)
            if enemy.lvl == 1:
                request.user.balance += random.randint(20,50)
            elif enemy.lvl == 2:
                request.user.balance += random.randint(120,250)
            elif enemy.lvl == 3:
                request.user.balance += random.randint(220,350)
            self.request.user.save()
            enemy.delete()
            html = render_to_string(request=request,template_name='BK/win.html')
            return JsonResponse({"html":html},status=200)
        html = render_to_string(request=request,template_name='BK/fight.html',context={'enemy':enemy,'form':form_class,'msg_at':msg_at,'msg_def':msg_def,'msg_bot_a':msg_enemy_at,'msg_bot_def':msg_enemy_def})
        return JsonResponse({"html":html},status=200)


    
    def test_func(self):
        user = Newuser.objects.get(pk=self.kwargs['pk'])
        return self.request.user==user

class BossFight(LoginRequiredMixin,UserPassesTestMixin,View):

    def get(self,request,*args, **kwargs):
        form_class = AttackF()
        if request.user.is_fight==False:
            request.user.is_fight = True
            if request.user.dungeon_lvl == 1:
                enemy = Enemy.objects.create(name="BOSS_lvl_1",health=150,attack=20,defence=17,lvl=98,img="enemy/first.png",slug=request.user.username)
            elif request.user.dungeon_lvl == 2:
                enemy = Enemy.objects.create(name="BOSS_lvl_2",attack=45,health=200,defence=36,lvl=99,img="enemy/second.png",slug=request.user.username,weapon=Weapon.objects.get(pk=2),armor=Armor.objects.get(pk=2))
            elif request.user.dungeon_lvl == 3:
                enemy = Enemy.objects.create(name="BOSS_lvl_3",attack=60,defence=55,health=300,lvl=100,img="enemy/third.png",slug=request.user.username,weapon=Weapon.objects.get(pk=4),armor=Armor.objects.get(pk=4))
            request.user.enemy = enemy
            request.user.save()
            return render(request,'BK/boss_fight.html',context={'enemy':enemy,'form':form_class})
        else:
            enemy = Enemy.objects.get(slug=request.user.username)
            return render(request,'BK/boss_fight.html',context={'enemy':enemy,'form':form_class})
    
    def post(self,request,*args, **kwargs):
        form_class = AttackF(request.POST)
        enemy = Enemy.objects.get(slug=request.user.username)
        choic = {0:'head',1:'body',2:'legs'}
        selat = random.randint(0,2)
        seldef = random.randint(0,2)
        if request.POST['attack'] == choic[seldef]:
            msg_enemy_def = "Boss blocked your atack!"
            msg_at = ""
        else:
            if request.user.ReturnAllDamage() - (int(enemy.ReturnAllArmor()/2))>=0:    
                enemy.health -= request.user.ReturnAllDamage() - (int(enemy.ReturnAllArmor()/2))
                enemy.save()
                msg_enemy_def = ""
                msg_at = f"Your atack ({request.POST['attack']}) is success (-{request.user.ReturnAllDamage() - (int(enemy.ReturnAllArmor()/2))})"
            else:
                msg_enemy_def = ""
                msg_at = f"Your atack ({request.POST['attack']}) is success (0)"
        if request.POST['defence'] == choic[selat]:
            msg_def = "You blocked enemy atack!"
            msg_enemy_at = ""
        else:
            if enemy.ReturnAllDamage() - (int(request.user.ReturnAllArmor()/2))>=0:
                request.user.health -= enemy.ReturnAllDamage() - (int(request.user.ReturnAllArmor()/2))
                request.user.save()
                msg_def = ""
                msg_enemy_at = f"Boss atack ({choic[selat]}) is success (-{enemy.ReturnAllDamage() - (int(request.user.ReturnAllArmor()/2))})"
            else:
                msg_def = ""
                msg_enemy_at = f"Boss atack ({choic[selat]}) is success (0)"
        if request.user.health <= 0:
            request.user.health = 0
            request.user.dungeon_loc = 0
            request.user.is_fight = False
            self.request.user.save()
            enemy.delete()
            html = render_to_string(request=request,template_name='BK/boss_lose.html')
            return JsonResponse({"html":html},status=200)
        elif enemy.health <= 0:
            request.user.is_fight = False
            request.user.dungeon_loc = 0
            request.user.dungeon_lvl += 1
            if enemy.lvl == 98:
                lvl = "First"
                pay = 1250
                request.user.balance += pay
            elif enemy.lvl == 99:
                lvl = "Second"
                pay = 2550
                request.user.balance += pay
            elif enemy.lvl == 100:
                pay = 4150
                lvl = "Final"
                request.user.balance += pay
            self.request.user.save()
            enemy.delete()
            html = render_to_string(request=request,template_name='BK/boss_win.html',context={'lvl':lvl,'rew':pay})
            return JsonResponse({"html":html},status=200)
        html = render_to_string(request=request,template_name='BK/boss_fight.html',context={'enemy':enemy,'form':form_class,'msg_at':msg_at,'msg_def':msg_def,'msg_bot_a':msg_enemy_at,'msg_bot_def':msg_enemy_def})
        return JsonResponse({"html":html},status=200)

    
    def test_func(self):
        user = Newuser.objects.get(pk=self.kwargs['pk'])
        return self.request.user==user