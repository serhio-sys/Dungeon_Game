from django import forms

class AttackF(forms.Form):
    choise = [("head","head"),
            ("body","body"),
            ("legs","legs"),
            ]
    attack = forms.CharField(label="ATACK",widget=forms.RadioSelect(choices=choise))
    defence = forms.CharField(label="DEFENCE",widget=forms.RadioSelect(choices=choise))