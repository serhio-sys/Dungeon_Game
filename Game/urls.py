from django.urls import path
from .views import *

urlpatterns = [
    path('location1/',Location1.as_view(),name='loc1'),
    path('location2/',Location2.as_view(),name='loc2'),
    path('location2/sleeproom/',SleepRoom.as_view(),name='sleep'),
    path('sleeped/',Sleepes.as_view(),name="sleeped"),
    path('sleeping/<pk>/',Sleeping,name="sleeping"),
    path('location3/',Location3.as_view(),name='loc3'),
    path('location3/shop/',Shop.as_view(),name='shop'),
    path('buy-weapon/<int:weapon>/',buyweapon,name='buy_w'),
    path('buy-armor/<int:armor>/',buyarmor,name='buy_a'),
    path('successbuy/',SuccesBuy.as_view(),name='success_b'),
    path('location4/',Location4.as_view(),name='loc4'),
    path('dungeon/',Dungeon.as_view(),name='dungeon'),
    path('dungeon_go/',DungeonGo.as_view(),name='dungeon_go'),
    path('dungeon_go/Location1',Dungeon_Loc1.as_view(),name='dun_loc1'),
    path('dungeon_go/Location2',Dungeon_Loc2.as_view(),name='dun_loc2'),
    path('dungeon_go/Location3',Dungeon_Loc3.as_view(),name='dun_loc3'),
    path('dungeon_go/Location4',Dungeon_Loc4.as_view(),name='dun_loc4'),
    path('healing',Healing.as_view(),name='heal'),
    path('dungeon_go/payed/',PayBadGuys.as_view(),name='pay'),
    path('dungeon_go/take/',TakeTreasure.as_view(),name='take'),
    path('dungeon_go/fight/<pk>/',Fight.as_view(),name='fight'),
    path('dungeon_go/<pk>/bossfight/',BossFight.as_view(),name='bossfight'),
] 
