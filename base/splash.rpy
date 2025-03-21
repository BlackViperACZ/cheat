label after_load:

    if discordrun:
        python:
            try:
                import io
                import os
                io.open("game/state.txt", 'w+', encoding = "utf-8").write(state)
            except:
                import io
                try:
                    open("game/state.txt", 'w+')
                    io.open("game/state.txt", 'w+', encoding = "utf-8").write("err3")
                    state = "err3"
                except:
                    pass

    $ save_name = persistent.current_save_name
    $ updateRewardLists()
    if renpy.loadable("dev/dev_screens.rpyc"):
        show screen dev_screen
    
    if persistent.mod_wtenabled == None:
       #$ del persistent.mod_wtenabled
       $ persistent.mod_wtenabled = True
    if persistent.mod_wt_enabled == None:
       #$ del persistent.mod_wtenabled
       $ persistent.mod_wt_enabled = True
    $ persistent.mod_wt_enabled = True   
    if not hasattr(store,"branchIsabella"):
       $branchIsabella=False
    if not hasattr(store,"branchSage"):
       $branchSage=False
    if not hasattr(store,"branchMayaJosy"):
       $branchMayaJosy=False
    if not hasattr(store,"branchJill"):
       $ branchJill=False
    if not hasattr(store,"branchAlone"):
       $branchAlone=False
    if not hasattr(store,"jade_state"):
       $ jade_state = 0
    return

label before_main_menu:

    if discordrun:
        python:
            import io
            state = "mm"
            try:
                io.open("game/state.txt", 'w+', encoding = "utf-8").write(state)
            except:
                pass

    return

label quit:

    if discordrun:
        python:
            import os
            os.popen('taskkill /f /im python.exe')

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
