class Coffee
    def initialize(temp = 0, flavor = 'bland')
        @temperature = temp
        @flavor = flavor
    end

    def temp!(temp)
        @temperature = 
        temp
    end

    def hot?(temp)
        if temp > 160
            return true
        end

        false
    end

    def display_temp
        puts @temperature
    end
end

c = Coffee.new(90)
puts c.hot?(170)