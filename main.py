from strength_checker import check_strength
from db_utils import check_reuse
from suggestions import hidden_input, generate_strong_password

if __name__ == "__main__":
    print("\n🔐 Welcome to the Password Analyzer 🔐")
    print("======================================")

    # Show guaranteed strong suggestion first
    suggestion = generate_strong_password()
    print(f"\n Suggested strong password: {suggestion}")

    # Ask if user wants to use it
    choice = input("\nDo you want to use the Suggested Password? (Yes/No): ").strip().lower()

    if choice == "yes":
        pwd = suggestion
        print("\n You Chose the Suggested Password ")
        if check_reuse(pwd):
            print("⚠️ This Password has been Used Before.")
        else:
            print(" Strength Score: 5/5 ")
            print("✅ The New Password has been Saved Successfully.")
        
    else:
        pwd = hidden_input("\nEnter your password: ")
        strength, feedback = check_strength(pwd)

        if check_reuse(pwd):
            print("\n⚠️ This Password has been Used Before.")
        else:
            print("✅ The New Password has been Saved Successfully.")

        print(f" Strength Score: {strength}/5 ")
        if feedback:
            print("\n Suggestions to improve:")
            for f in feedback:
                print(" -", f)
        else:
            print("\n Your password is strong! 🎉")

    print("\n======================================")
    print("🔒 Analysis complete. Stay secure! 🔒\n")
