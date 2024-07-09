from typing import Any
import flet as ft
import sys,os
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
    TextField
    )

from model.tennismatch import TennisMatch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from service.match_service import update_match
import config

class ScoreboardStream(UserControl):
    def __init__(self, match: TennisMatch, page: ft.Page):
        super().__init__()
        self.match = match
        self.page = page
        self.placar_1 = Row(
            spacing=0,
        )
        self.placar_2 = Row(
            spacing=0,
        )

        self.topic_name = "match_topic_"+str(self.match.match_id)
        page.pubsub.subscribe_topic(self.topic_name, self.on_score_updated)

    def update_placar_1(self):
        self.placar_1.controls.clear()
        #Nome do jogador
        self.placar_1.controls.append(
            ft.Container(
                content=ft.Text(size=14,value=self.match.player1.upper(), color=colors.WHITE,weight=ft.FontWeight.W_900,width=90,max_lines=2),
                alignment=ft.alignment.center,
                
                padding=5,
                height=50,
                width=90,
                gradient=ft.RadialGradient(
                    center=ft.alignment.bottom_right,
                    colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                    radius=1,
                ),
                #border_radius=ft.border_radius.all(5),
            ),
        )

        #Sets finalizados
        for set in self.match.match_moment.sets:
            self.placar_1.controls.append(
                ft.Container(
                    content=ft.Text(value=set.player1_score, color=colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2),
                    alignment=ft.alignment.center,
                    padding=5,
                    height=50,
                    width=30,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[config.MAIN_COLOR_2,config.MAIN_COLOR_1,],
                        
                    ),
                    #border_radius=ft.border_radius.all(5),
                )
            )
        #Set em andamento
        self.placar_1.controls.append(
            ft.Container(
                        content=ft.Text(value=self.match.match_moment.current_set.player1_score, color=colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2),
                        alignment=ft.alignment.center,
                        padding=10,
                        height=50,
                        width=31,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[config.CURRENT_SET_COLOR_1,config.CURRENT_SET_COLOR_2,],
                            
                        ),
                        border_radius=ft.border_radius.all(5),
                    )
        )

        #Game em andamento
        self.placar_1.controls.append(
            ft.Container(
                content=ft.Text(
                    value=self.match.match_moment.current_game.player1_score,
                    color=colors.GREY_800,
                    weight=ft.FontWeight.BOLD,
                    width=100,
                    max_lines=2,
                    text_align=ft.TextAlign.CENTER,
                    ),
                alignment=ft.alignment.center,
                width=51.6,
                height=50,
                #bgcolor=ft.colors.WHITE,
                border_radius=ft.border_radius.all(5),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[config.CURRENT_GAME_COLOR_1,config.CURRENT_GAME_COLOR_2,],
                ),
            )
        )

    def update_placar_2(self):
        self.placar_2.controls.clear()
        #Nome do jogador
        self.placar_2.controls.append(
            ft.Container(
                content=ft.Text(size=14,value=self.match.player2.upper(), color=colors.WHITE,weight=ft.FontWeight.W_900,width=90,max_lines=2),
                alignment=ft.alignment.center,
                
                padding=5,
                height=50,
                width=90,
                gradient=ft.RadialGradient(
                    center=ft.alignment.bottom_right,
                    colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                    radius=1,
                ),
                #border_radius=ft.border_radius.all(5),
            ),
        )

        #Sets finalizados
        for set in self.match.match_moment.sets:
            self.placar_2.controls.append(
                ft.Container(
                    content=ft.Text(value=set.player2_score, color=colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2),
                    alignment=ft.alignment.center,
                    padding=5,
                    height=50,
                    width=30,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[config.MAIN_COLOR_2,config.MAIN_COLOR_1,],
                        
                    ),
                    #border_radius=ft.border_radius.all(5),
                )
            )

        #Set em andamento
        self.placar_2.controls.append(
            ft.Container(
                content=ft.Text(value=self.match.match_moment.current_set.player2_score, color=colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2),
                alignment=ft.alignment.center,
                padding=10,
                height=50,
                width=31,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[config.CURRENT_SET_COLOR_1,config.CURRENT_SET_COLOR_2,],
                    
                ),
                border_radius=ft.border_radius.all(5),
            )
        )

        #Game em andamento
        self.placar_2.controls.append(
            ft.Container(
                content=ft.Text(
                    value=self.match.match_moment.current_game.player2_score,
                    color=colors.GREY_800,
                    weight=ft.FontWeight.BOLD,
                    width=100,
                    max_lines=2,
                    text_align=ft.TextAlign.CENTER,
                    ),
                alignment=ft.alignment.center,
                width=51.6,
                height=50,
                #bgcolor=ft.colors.WHITE,
                border_radius=ft.border_radius.all(5),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[config.CURRENT_GAME_COLOR_1,config.CURRENT_GAME_COLOR_2,],
                ),
            )
        )
    
    def on_score_updated(self, e, match):
        self.match=match
        self.update_placar_1()
        self.update_placar_2()
        self.update()

    

    def build(self):
        
    ## Criacao do placar
        self.update_placar_1()
        self.update_placar_2()
        #self.page.on_event("score_updated", self.on_score_updated)

    ## Texto dos botões grandes de pontuação
        return ft.SafeArea(
 
            content= 
            Container(
                        #width=300,
                        #height=450,
                        bgcolor=ft.colors.TRANSPARENT,
                        #border_radius=border_radius.all(5),
                        padding=4,
                        content=Column(
                            spacing=50,
                            controls=[                 
#================================== PLACAR =======================================                              
                                Row(
                                    controls=[
                                        Container(
                                            expand=1,
                                            bgcolor=colors.TRANSPARENT,
                                            border_radius=border_radius.all(5),
                                            #height=100,
                                            content = Column(
                                                spacing =0,
                                                controls = [
                                                    self.placar_1,
                                                    self.placar_2,
                                                ],
                                            ),
                                        )
                                    ]
                                ),
#================================
                                
                            ],
                        ),
                    ),
            )
        