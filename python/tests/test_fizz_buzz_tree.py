from code_challenges.fizz_buzz_tree.fizz_buzz_tree import KAry_tree, KNode

# def test_KAry_tree_and_KNode_import():
    # assert KAry_tree and KNode

# def test_KAry_tree_add_initial_value():
#     k_tree = KAry_tree()
#     k_tree.add('babies')
#     assert k_tree.root.value == 'babies'

# def test_KAry_tree_add_multiple_unordered():
#     k_tree = KAry_tree()
#     k_tree.add('babies')
#     k_tree.add('chickens')
#     assert isinstance(k_tree.root.children['chickens'], KNode)

def test_work_please_please_please():
    k_tree = KAry_tree()
    k_tree.add('babies')
    k_tree.add('yeti')
    k_tree.add('sasquatch')
    k_tree.add('mythical beasts')
    assert 'mythical beasts' in k_tree.root.children

# def test_add_with_passing_in_node():
#     k_tree = KAry_tree()
#     node = KNode('chickens', {'babies': None})
#     k_tree.add('chickens', node)
#     k_tree.add('babies')
#     k_tree.add('yeti')
#     k_tree.add('sasquatch')
#     k_tree.add('mythical beasts')
#     assert k_tree.root.children['babies'].value == 'babies'
