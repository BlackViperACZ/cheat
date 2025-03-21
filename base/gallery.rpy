init:
    $ persistent.totalWallpapers = 16
    $ persistent.totalScenes = 54


    if persistent.epi_lewd_zoey == None:
        $ persistent.epi_lewd_zoey = False
    if persistent.epi_lewd_eb == None:
        $ persistent.epi_lewd_eb = False


    if persistent.ep9_lewd_jade == None:
        $ persistent.ep9_lewd_jade = False
    if persistent.ep9_lewd_jill == None:
        $ persistent.ep9_lewd_jill = False
    if persistent.ep9_lewd_sage1 == None:
        $ persistent.ep9_lewd_sage1 = False
    if persistent.ep9_lewd_lily == None:
        $ persistent.ep9_lewd_lily = False
    if persistent.ep9_lewd_sage2 == None:
        $ persistent.ep9_lewd_sage2 = False
    if persistent.ep9_lewd_maya == None:
        $ persistent.ep9_lewd_maya = False
    if persistent.ep9_lewd_camila == None:
        $ persistent.ep9_lewd_camila = False
    if persistent.ep9_lewd_heather == None:
        $ persistent.ep9_lewd_heather = False
    if persistent.ep9_lewd_cumpetition == None:
        $ persistent.ep9_lewd_cumpetition = False
    if persistent.ep9_lewd_isabella == None:
        $ persistent.ep9_lewd_isabella = False
    if persistent.ep9_lewd_jm2 == None:
        $ persistent.ep9_lewd_jm2 = False
    if persistent.ep9_lewd_isabella2 == None:
        $ persistent.ep9_lewd_isabella2 = False
    if persistent.ep9_lewd_jill2 == None:
        $ persistent.ep9_lewd_jill2 = False
    if persistent.ep9_lewd_jm == None:
        $ persistent.ep9_lewd_jm = False
    if persistent.ep9_lewd_sage3 == None:
        $ persistent.ep9_lewd_sage3 = False
    if persistent.ep9_lewd_ln == None:
        $ persistent.ep9_lewd_ln = False
    if persistent.ep9_lewd_quinn == None:
        $ persistent.ep9_lewd_quinn = False
    if persistent.ep9_lewd_sm == None:
        $ persistent.ep9_lewd_sm = False


    if persistent.ep10_lewd_cathy == None:
        $ persistent.ep10_lewd_cathy = False
    if persistent.ep10_lewd_madame1 == None:
        $ persistent.ep10_lewd_madame1 = False
    if persistent.ep10_lewd_madame2 == None:
        $ persistent.ep10_lewd_madame2 = False
    if persistent.ep10_lewd_madame3 == None:
        $ persistent.ep10_lewd_madame3 = False
    if persistent.ep10_lewd_josy == None:
        $ persistent.ep10_lewd_josy = False
    if persistent.ep10_lewd_jm == None:
        $ persistent.ep10_lewd_jm = False
    if persistent.ep10_lewd_maya == None:
        $ persistent.ep10_lewd_maya = False
    if persistent.ep10_lewd_sage == None:
        $ persistent.ep10_lewd_sage = False
    if persistent.ep10_lewd_sage2 == None:
        $ persistent.ep10_lewd_sage2 = False
    if persistent.ep10_lewd_jill == None:
        $ persistent.ep10_lewd_jill = False
    if persistent.ep10_lewd_isabella == None:
        $ persistent.ep10_lewd_isabella = False
    if persistent.ep10_lewd_nicole == None:
        $ persistent.ep10_lewd_nicole = False
    if persistent.ep10_lewd_riona == None:
        $ persistent.ep10_lewd_riona = False
    if persistent.ep10_lewd_nora == None:
        $ persistent.ep10_lewd_nora = False
    if persistent.ep10_lewd_lily == None:
        $ persistent.ep10_lewd_lily = False
    if persistent.ep10_lewd_quinn == None:
        $ persistent.ep10_lewd_quinn = False


    if persistent.ep11_lewd_camila == None:
        $ persistent.ep11_lewd_camila = False
    if persistent.ep11_lewd_sarah == None:
        $ persistent.ep11_lewd_sarah = False
    if persistent.ep11_lewd_melanie == None:
        $ persistent.ep11_lewd_melanie = False
    if persistent.ep11_lewd_lynette == None:
        $ persistent.ep11_lewd_lynette = False
    if persistent.ep11_lewd_jade == None:
        $ persistent.ep11_lewd_jade = False
    if persistent.ep11_lewd_madame == None:
        $ persistent.ep11_lewd_madame = False
    if persistent.ep11_lewd_bella == None:
        $ persistent.ep11_lewd_bella = False
    if persistent.ep11_lewd_jill == None:
        $ persistent.ep11_lewd_jill = False
    if persistent.ep11_lewd_bella2 == None:
        $ persistent.ep11_lewd_bella2 = False
    if persistent.ep11_lewd_jm == None:
        $ persistent.ep11_lewd_jm = False
    if persistent.ep11_lewd_tiffani == None:
        $ persistent.ep11_lewd_tiffani = False
    if persistent.ep11_lewd_tara == None:
        $ persistent.ep11_lewd_tara = False
    if persistent.ep11_lewd_becky == None:
        $ persistent.ep11_lewd_becky = False
    if persistent.ep11_lewd_lily == None:
        $ persistent.ep11_lewd_lily = False
    if persistent.ep11_lewd_elena == None:
        $ persistent.ep11_lewd_elena = False
    if persistent.ep11_lewd_sage == None:
        $ persistent.ep11_lewd_sage = False
    if persistent.ep11_lewd_sage2 == None:
        $ persistent.ep11_lewd_sage2 = False
    if persistent.ep11_lewd_jill2 == None:
        $ persistent.ep11_lewd_jill2 = False
        
default wt_gall_char="All"        
default gall_chars_list=["Sage","Maya","Josy","Jill","Isabella","Quinn","Riona","Camila","Sarah","Melanie","Jade","Nicole","Lily","Cathy","Zoey","Heather","Madame","Nora","Tara","Tiffani","All"]

screen gall_char_filter():
   modal True
       
   frame:
         xpos 0.36
         ypos 0.00
         xsize 0.15
         vpgrid:
             xsize 200
             cols 1
             for index,i in enumerate(gall_chars_list):
               vbox:
                 textbutton "[i]" action [SetVariable("wt_gall_char",i),Hide("gall_char_filter")] text_size 27

screen scenes:
    tag menu

    add "rewards/general/rewards_new_bg.jpg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "rewards/general/rewards_new_fg3.png"
    imagebutton:
        idle "rewards/general/rew_x_idle.png"
        hover "rewards/general/rew_x_hover.png"
        action Return()
        xalign 0.99
        yalign 0.00
    key "mouseup_2" action Return()
    text "Scenes" style "reward_header_style" xalign 0.02 yalign 0.005
    textbutton "Character Filter" action Show("gall_char_filter") xalign 0.45 yalign 0.005 text_size 40
    vpgrid:
        ypos 0.085

        ysize 0.898
        yoffset 2
        cols 5
        spacing 10
        draggable True
        mousewheel True

        scrollbars "vertical"
        side_xalign 0.5

        if persistent.epi_lewd_zoey:
          if(wt_gall_char == "Zoey" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/epi_zoey.png")
                    hover Transform ("images/gallery/epi_zoey_hover.png")
                    action Replay("epi_zoey_lewd_label")
                text "Interlude - Zoey" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Interlude - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.epi_lewd_eb:
          if(wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/epi_emma.png")
                    hover Transform ("images/gallery/epi_emma_hover.png")
                    action Replay("epi_eb_lewd_label")
                text "Interlude - Emma" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Interlude - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_jade:
          if(wt_gall_char == "Jade" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_jade.png")
                    hover Transform ("images/gallery/ep9_jade_hover.png")
                    action Replay("ep9_jade_lewd_label")
                text "Episode 9 - Jade" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_jill:
          if(wt_gall_char == "Jill" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_jill.png")
                    hover Transform ("images/gallery/ep9_jill_hover.png")
                    action Replay("ep9_jill_lewd_label")
                text "Episode 9 - Jill" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        if persistent.ep9_lewd_sage1:
          if(wt_gall_char == "Sage" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_sage.png")
                    hover Transform ("images/gallery/ep9_sage_hover.png")
                    action Replay("ep9_sage_lewd1_label")
                text "Episode 9 - Sage" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        if persistent.ep9_lewd_lily:
          if(wt_gall_char == "Lily" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_lily.png")
                    hover Transform ("images/gallery/ep9_lily_hover.png")
                    action Replay("ep9_lily_lewd_label")
                text "{size=-3}Episode 9 - Lily{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_sage2:
          if(wt_gall_char == "Sage" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_sage2.png")
                    hover Transform ("images/gallery/ep9_sage2_hover.png")
                    action Replay("ep9_sage_lewd2_label")
                text "Episode 9 - Sage" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_maya:
          if(wt_gall_char == "Maya" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_maya.png")
                    hover Transform ("images/gallery/ep9_maya_hover.png")
                    action Replay("ep9_msolo_lewd_label")
                text "Episode 9 - Maya" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_camila:
          if(wt_gall_char == "Camila" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_camila.png")
                    hover Transform ("images/gallery/ep9_camila_hover.png")
                    action Replay("ep9_diks_ph2_camila_dance_event_label")
                text "{size=-3}Episode 9 - Camila{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_heather:
          if(wt_gall_char == "Heather" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_heather.png")
                    hover Transform ("images/gallery/ep9_heather_hover.png")
                    action Replay("ep9_diks_ph3_heather_event_label")
                text "{size=-5}Episode 9 - Heather{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        if persistent.ep9_lewd_cumpetition:
          if(wt_gall_char == "Nicole" or wt_gall_char == "Lily" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_cumpetition.png")
                    hover Transform ("images/gallery/ep9_cumpetition_hover.png")
                    action Replay("ep9_diks_ph3_cumpetition_event2_label")
                text "{size=-11}Episode 9 - CUM-petition{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        if persistent.ep9_lewd_isabella:
          if(wt_gall_char == "Isabella" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_isabella.png")
                    hover Transform ("images/gallery/ep9_isabella_hover.png")
                    action Replay("ep9_bsolo_label")
                text "{size=-3}Episode 9 - Isabella{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_jm2:
          if(wt_gall_char == "Josy" or wt_gall_char == "Maya" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_jm2.png")
                    hover Transform ("images/gallery/ep9_jm2_hover.png")
                    action Replay("ep9_diks_ph3_mj_event2_label")
                text "{size=-9}Episode 9 - Josy & Maya{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        if persistent.ep9_lewd_isabella2:
          if(wt_gall_char == "Isabella" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_isabella2.png")
                    hover Transform ("images/gallery/ep9_isabella2_hover.png")
                    action Replay("ep9_bella_lewd2_label")
                text "{size=-3}Episode 9 - Isabella{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_jill2:
          if(wt_gall_char == "Jill" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_jill2.png")
                    hover Transform ("images/gallery/ep9_jill2_hover.png")
                    action Replay("ep9_jill_lewd2_label")
                text "Episode 9 - Jill" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_jm:
          if(wt_gall_char == "Josy" or wt_gall_char == "Maya" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_jm.png")
                    hover Transform ("images/gallery/ep9_jm_hover.png")
                    action Replay("ep9_jm_lewd_label")
                text "{size=-9}Episode 9 - Josy & Maya{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_sage3:
          if(wt_gall_char == "Sage" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_sage3.png")
                    hover Transform ("images/gallery/ep9_sage3_hover.png")
                    action Replay("ep9_sage_lewd3_label")
                text "Episode 9 - Sage" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_ln:
          if(wt_gall_char == "Lily" or wt_gall_char == "Nicole" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_ln.png")
                    hover Transform ("images/gallery/ep9_ln_hover.png")
                    action Replay("ep9_lily_nicole_lewd_label")
                text "{size=-9}Episode 9 - Lily & Nicole{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_quinn:
          if(wt_gall_char == "Quinn" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_quinn.png")
                    hover Transform ("images/gallery/ep9_quinn_hover.png")
                    action Replay("ep9_quinn_lewd_label")
                text "{size=-3}Episode 9 - Quinn{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep9_lewd_sm:
          if(wt_gall_char == "Sarah" or wt_gall_char == "Melanie" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep9_sm.png")
                    hover Transform ("images/gallery/ep9_sm_hover.png")
                    action Replay("ep9_sm_lewd_label")
                text "{size=-9}Episode 9 - Sarah & Mel{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-3}Episode 9 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_madame1:
          if(wt_gall_char == "Madame" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_madame1.png")
                    hover Transform ("images/gallery/ep10_madame1_hover.png")
                    action Replay("ep10_madame_boobjob_lewd_label")
                text "{size=-4}Ep 10 - {size=-2}Madame{/size}{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_madame2:
          if(wt_gall_char == "Madame" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_madame2.png")
                    hover Transform ("images/gallery/ep10_madame2_hover.png")
                    action Replay("ep10_madame_footjob_lewd_label")
                text "{size=-4}Ep 10 - {size=-2}Madame{/size}{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_madame3:
          if(wt_gall_char == "Madame" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_madame3.png")
                    hover Transform ("images/gallery/ep10_madame3_hover.png")
                    action Replay("ep10_madame_fuck_lewd_label")
                text "{size=-4}Ep 10 - {size=-2}Madame{/size}{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_quinn:
          if(wt_gall_char == "Quinn" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_quinn.png")
                    hover Transform ("images/gallery/ep10_quinn_hover.png")
                    action Replay("ep10_quinn_lewd_label")
                text "{size=-5}Episode 10 - Quinn{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_maya:
          if(wt_gall_char == "Maya" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_maya.png")
                    hover Transform ("images/gallery/ep10_maya_hover.png")
                    action Replay("ep10_maya_lewd_label")
                text "{size=-5}Episode 10 - Maya{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_josy:
          if(wt_gall_char == "Josy" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_josy.png")
                    hover Transform ("images/gallery/ep10_josy_hover.png")
                    action Replay("ep10_josy_lewd_label")
                text "Episode 10 - Josy" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_jill:
          if(wt_gall_char == "Jill" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_jill.png")
                    hover Transform ("images/gallery/ep10_jill_hover.png")
                    action Replay("ep10_jill_lewd_label")
                text "Episode 10 - Jill" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_nora:
          if(wt_gall_char == "Nora" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_nora.png")
                    hover Transform ("images/gallery/ep10_nora_hover.png")
                    action Replay("ep10_nora_lewd_label")
                text "{size=-5}Episode 10 - Nora{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_nicole:
          if(wt_gall_char == "Nicole" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_nicole.png")
                    hover Transform ("images/gallery/ep10_nicole_hover.png")
                    action Replay("ep10_nicole_lewd_label")
                text "{size=-5}Episode 10 - Nicole{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_isabella:
          if(wt_gall_char == "Isabella" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_isabella.png")
                    hover Transform ("images/gallery/ep10_isabella_hover.png")
                    action Replay("ep10_isabella_lewd_label")
                text "{size=-5}Episode 10 - Isabella{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_cathy:
          if(wt_gall_char == "Cathy" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_cathy.png")
                    hover Transform ("images/gallery/ep10_cathy_hover.png")
                    action Replay("ep10_cathy_lewd_label")
                text "{size=-5}Episode 10 - Cathy{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_sage:
          if(wt_gall_char == "Sage" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_sage.png")
                    hover Transform ("images/gallery/ep10_sage_hover.png")
                    action Replay("ep10_sage_lewd_label")
                text "{size=-5}Episode 10 - Sage{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_riona:
          if(wt_gall_char == "Riona" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_riona.png")
                    hover Transform ("images/gallery/ep10_riona_hover.png")
                    action Replay("ep10_riona_lewd_label")
                text "{size=-5}Episode 10 - Riona{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_lily:
          if(wt_gall_char == "Lily" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_lily.png")
                    hover Transform ("images/gallery/ep10_lily_hover.png")
                    action Replay("ep10_lily_lewd_label")
                text "Episode 10 - Lily" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_jm:
          if(wt_gall_char == "Josy" or wt_gall_char == "Maya" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_jm.png")
                    hover Transform ("images/gallery/ep10_jm_hover.png")
                    action Replay("ep10_jm_lewd_label")
                text "{size=-10}Episode 10 - Josy & Maya{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep10_lewd_sage2:
          if(wt_gall_char == "Sage" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep10_sage2.png")
                    hover Transform ("images/gallery/ep10_sage2_hover.png")
                    action Replay("ep10_bbq_sage_lewd_label")
                text "{size=-5}Episode 10 - Sage{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 10 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_camila:
          if(wt_gall_char == "Camila" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_camila.png")
                    hover Transform ("images/gallery/ep11_camila_hover.png")
                    action Replay("ep11_camila_lewd_label")
                text "{size=-5}Episode 11 - Camila{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        if persistent.ep11_lewd_sarah:
          if(wt_gall_char == "Sarah" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_sarah.png")
                    hover Transform ("images/gallery/ep11_sarah_hover.png")
                    action Replay("ep11_sarah_lewd_label")
                text "{size=-5}Episode 11 - Sarah{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        if persistent.ep11_lewd_melanie:
          if(wt_gall_char == "Melanie" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_melanie.png")
                    hover Transform ("images/gallery/ep11_melanie_hover.png")
                    action Replay("ep11_melanie_lewd_label")
                text "{size=-5}Episode 11 - Melanie{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        if persistent.ep11_lewd_lynette:
          if(wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_lynette.png")
                    hover Transform ("images/gallery/ep11_lynette_hover.png")
                    action Replay("ep11_diary_lewd_label")
                text "{size=-5}Episode 11 - Lynette{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_jade:
          if(wt_gall_char == "Jade" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_jade.png")
                    hover Transform ("images/gallery/ep11_jade_hover.png")
                    action Replay("ep11_jade_lewd_label")
                text "{size=-5}Episode 11 - Jade{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_madame:
          if(wt_gall_char == "Madame" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_madame.png")
                    hover Transform ("images/gallery/ep11_madame_hover.png")
                    action Replay("ep11_madame_anal_lewd_label")
                text "{size=-4}Ep 11 - {size=-2}Madame{/size}{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_bella:
          if(wt_gall_char == "Isabella" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_bella.png")
                    hover Transform ("images/gallery/ep11_bella_hover.png")
                    action Replay("ep11_bella_lewd_label")
                text "{size=-5}Episode 11 - Bella{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_jill:
          if(wt_gall_char == "Jill" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_jill.png")
                    hover Transform ("images/gallery/ep11_jill_hover.png")
                    action Replay("ep11_jill_lewd_label")
                text "Episode 11 - Jill" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_bella2:
          if(wt_gall_char == "Isabella" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_bella2.png")
                    hover Transform ("images/gallery/ep11_bella2_hover.png")
                    action Replay("ep11_bella2_lewd_label")
                text "{size=-5}Episode 11 - Bella{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_jm:
          if(wt_gall_char == "Maya" or wt_gall_char=="Josy" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_jm.png")
                    hover Transform ("images/gallery/ep11_jm_hover.png")
                    action Replay("ep11_jm_lewd_label")
                text "{size=-10}Episode 11 - Josy & Maya{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_tiffani:
          if(wt_gall_char=="Tiffani" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_tiffani.png")
                    hover Transform ("images/gallery/ep11_tiffani_hover.png")
                    action Replay("ep11_tiffani_lewd_label")
                text "{size=-5}Episode 11 - Tiffani{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_tara:
          if(wt_gall_char == "Tara" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_tara.png")
                    hover Transform ("images/gallery/ep11_tara_hover.png")
                    action Replay("ep11_tara_lewd_label")
                text "{size=-5}Episode 11 - Tara{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_becky:
          if(wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_becky.png")
                    hover Transform ("images/gallery/ep11_becky_hover.png")
                    action Replay("ep11_becky_lewd_label")
                text "{size=-5}Episode 11 - Becky{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_lily:
          if(wt_gall_char == "Lily" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_lily.png")
                    hover Transform ("images/gallery/ep11_lily_hover.png")
                    action Replay("ep11_lily_lewd_label")
                text "Episode 11 - Lily" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_elena:
          if(wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_elena.png")
                    hover Transform ("images/gallery/ep11_elena_hover.png")
                    action Replay("ep11_pp_elena_lewd_event_label")
                text "{size=-5}Episode 11 - Elena{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_sage:
          if(wt_gall_char == "Sage" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_sage.png")
                    hover Transform ("images/gallery/ep11_sage_hover.png")
                    action Replay("ep11_sage_lewd_label")
                text "{size=-5}Episode 11 - Sage{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_sage2:
          if(wt_gall_char == "Sage" or wt_gall_char== "Camila" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_sage2.png")
                    hover Transform ("images/gallery/ep11_sage2_hover.png")
                    action Replay("ep11_sage2_lewd_label")
                text "{size=-4}Ep 11 - {size=-6}Sage & Camila{/size}{/size}" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        if persistent.ep11_lewd_jill2:
          if(wt_gall_char == "Jill" or wt_gall_char == "All"):
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                imagebutton:
                    focus_mask True
                    idle Transform ("images/gallery/ep11_jill2.png")
                    hover Transform ("images/gallery/ep11_jill2_hover.png")
                    action Replay("ep11_jill2_lewd_label")
                text "Episode 11 - Jill" xalign 0.5 yalign 0.5 ypos 0.7
        else:
            vbox xalign 0.5 yalign 0.5:
                yminimum 200
                add "gallery/locked.png"
                text "{size=-5}Episode 11 - Locked{/size}" xalign 0.5 yalign 0.5 ypos 0.7

        vbox xalign 0.5 yalign 0.5:
            yminimum 200
            add "gallery/disabled_btn.png"
            text ""
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
