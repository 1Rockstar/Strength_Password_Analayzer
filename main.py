from strength_checker import check_strength
from db_utils import check_reuse
from suggestions import confirm_input, generate_strong_password

if __name__ == "__main__":
    print("\n🔐 Welcome to the Password Analyzer 🔐")
    print("======================================")

    # Show guaranteed strong suggestion first
    suggestion = generate_strong_password()
    print(f"\n Suggested strong password: {suggestion}")

    choice = input("\nDo you want to use the suggested password? (yes/no): ").strip().lower()

    if choice == "yes":
        pwd = suggestion
        print("\n✨ You chose the suggested password ✨")
        if check_reuse(pwd):
            print("⚠️ This password has been used before.")
            print("\n======================================")
        else:
            print("✅ The New Password Has Been Saved Succesfully.")
            print("\n======================================")
            
    else:
        pwd = confirm_input("\nEnter your password: ")
        strength, feedback = check_strength(pwd)

        if check_reuse(pwd):
            print("\n⚠️ This password has been used before.")
            print("\n======================================")
            
        else:
            print("✅ The New Password Has Been Saved Succesfully.")
            print(f" Strength Score: {strength}/5 ")
            if feedback:
                print("\n🔧 Suggestions to improve:")
                for f in feedback:
                    print(" -", f)
            else:
                print("\ Your password is strong! ")
            print("\n======================================")
    print("🔒 Analysis complete. Stay secure! 🔒\n")
