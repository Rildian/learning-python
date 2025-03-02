from module import sum, hello

# you can see the functions like this beucase i did "from archive import x,y"
hello()
print(sum(1, 2))

# but, if i just write "import module"
module.hello()
print(module.sum(1,2))

# its like writing a method.
# both will result the same outcome, 
# oh, apparently, if you use "import archive" you'll inherit EVERY function you've written
# from <module> import x, y... <- i've just chosen 2 here

