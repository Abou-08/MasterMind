import mastermind_graph as master



master.print_game(master.game)
master.canvas.bind("<Key>", master.on_key_press)
master.canvas.focus_set()
master.root.mainloop()
