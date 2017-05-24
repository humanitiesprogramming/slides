# let's annotate some code together.

class User
    def initialize(some_name = "anonymous", some_email = "none")
        # initializing an object from the user class. taking two arguments - a name and an email - and it assigns to attributes for the object. gives default settings if none are given. 
        @name = some_name
        @email = some_email
    end

    def display_name
        # prints the value assigned to the name attribute to the screen
        puts @name
    end

    def display_email
        # prints the email attribute to the screen.
        puts @email
    end

    def change_email!(new_email)
        # it has an exclamation point, so it's changing something. takes an argument and reassigns @email based on it.
        @email = new_email
    end

    def change_name!(new_name)
        # change the user's name.
        @name = new_name
    end

end

# create a new user, with 'brandon' and 'his old email'
brandon = User.new("brandon", "bmw9t@virginia.edu")
# print brandon's name
brandon.display_name
# print brandon's email
brandon.display_email
# changing brandon's email to ethan's.
brandon.change_email!("echreed@gmail.com")
# display my name again
brandon.display_email
# change brandon's name
brandon.change_name!("Ethan 'Boss Man' Reed")
# output it again.
brandon.display_name