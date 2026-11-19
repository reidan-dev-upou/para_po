START
    FUNC load_setup()
        LET output_dict = {
            "group_seed": get_group_seed(),
            "group_settings": get_group_settings(),
        }
        RETURN output_dict
    ENDFUNC

    FUNC update_setup_header()
        LET setup_header = MENU_SETUP_HEADER

        LET setup_header_dict = {
            "GROUP_NAME": GROUP_NAME,
            "MEMBER_NAMES": "AA, BB, CC",
            "GROUP_SEED": "00000",
            "BASE_FARE": "XXX",
            "EXTRA_FARE": "YY",
            "DISCOUNT_PERCENTAGE": "Z",
            "DATA_STOPS": "DD",
            "DATA_ROUTES": "EE",
        }

        FOR EACH (placeholder, actual_value) IN setup_header_dict DO
            setup_header = REPLACE placeholder WITH actual_value IN setup_header
        ENDFOR

        RETURN setup_header
    ENDFUNC

    FUNC show_setup_header()
        LET setup_header = update_setup_header()
        PRINT setup_header
    ENDFUNC

    FUNC read_menu_input()
        LET input_choice = INPUT "Enter choice (1-5): "

        WHILE TRUE DO
            IF input_choice IS DIGIT THEN
                IF 1 <= INT input_choice <= 5 THEN
                    BREAK
                ENDIF
                PRINT "Invalid input. Try again!"
            ELSE
                PRINT "Invalid input. Try again!"
            ENDIF

            input_choice = INPUT "Enter choice (1-5): "
        ENDWHILE

        RETURN INT input_choice
    ENDFUNC

    FUNC show_main_menu()
        WHILE TRUE DO
            PRINT MENU_OPTIONS
            LET input_choice = read_menu_input()

            IF input_choice == 1 THEN
                show_menu_1()
            ELSE IF input_choice == 2 THEN
                show_menu_2()
            ELSE IF input_choice == 3 THEN
                show_menu_3()
            ELSE IF input_choice == 4 THEN
                show_menu_4()
            ELSE IF input_choice == 5 THEN
                show_menu_5()
                BREAK
            ENDIF
        ENDWHILE
    ENDFUNC

    # main program
    FUNC main()
        LET setup_data = load_setup()
        show_setup_header()
        show_main_menu()
    ENDFUNC
END
