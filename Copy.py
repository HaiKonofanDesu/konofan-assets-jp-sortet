import shutil
import os.path

if __name__ == '__main__':
    current = os.getcwd();
    parent = os.path.dirname(current)
    source_dir = os.path.join(parent, "konofan-assets-jp-sortet", "Assets", "AddressableAssetsStore", "UnityAssets", "Common", "Images")
    destination_dir = os.path.join(current, "Assets", "AddressableAssetsStore", "UnityAssets", "Common", "Images")

    src_dir = os.path.join(source_dir, "IconAccessory")
    dst_dir = os.path.join(destination_dir, "IconAccessory")

    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)

    src_dir = os.path.join(source_dir, "IconAssist")
    dst_dir = os.path.join(destination_dir, "IconAssist")
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)

    src_dir = os.path.join(source_dir, "IconEnemy")
    dst_dir = os.path.join(destination_dir, "IconEnemy")
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)

    src_dir = os.path.join(source_dir, "IconLargeMember")
    dst_dir = os.path.join(destination_dir, "IconLargeMember")
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)

    src_dir = os.path.join(source_dir, "IconMember")
    dst_dir = os.path.join(destination_dir, "IconMember")
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)

    src_dir = os.path.join(source_dir, "IconMiddleMember")
    dst_dir = os.path.join(destination_dir, "IconMiddleMember")
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)

    src_dir = os.path.join(source_dir, "IconSpattack")
    dst_dir = os.path.join(destination_dir, "IconSpattack")
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)

    src_dir = os.path.join(source_dir, "IconWeapon")
    dst_dir = os.path.join(destination_dir, "IconWeapon")
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
