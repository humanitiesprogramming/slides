class User
    def initialize(some_name = "anonymous", some_email = "none")
        @name = some_name
        @email = some_email
    end

    def display_name
        puts @name
    end

    def display_email
        puts @email
    end

    def change_email!(new_email)
        @email = new_email
    end

end

brandon = User.new("brandon", "bmw9t@virginia.edu")
brandon.display_name
brandon.display_email
brandon.change_email!("echreed@gmail.com")
brandon.display_email