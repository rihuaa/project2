import unittest

from exp_eval import infix_to_postfix, postfix_eval, postfix_valid

class MyTest(unittest.TestCase):
    def test_reg_exp(self):
        exp = '3 * 2 + 5'
        post = infix_to_postfix(exp)
        self.assertEqual(post, '3 2 * 5 +')
        self.assertEqual(postfix_eval(post), 11)
        self.assertTrue(postfix_valid(post))

    def test_paran_exp(self):
        exp = '3 * ( 2 + 5 )'
        post = infix_to_postfix(exp)
        self.assertEqual(post, '3 2 5 + *')
        self.assertEqual(postfix_eval(post), 21)
        self.assertTrue(postfix_valid(post))

    def test_pow(self):
        exp = '3 ^ 2'
        post = infix_to_postfix(exp)
        self.assertEqual(post, '3 2 ^')
        self.assertEqual(postfix_eval(post), 9)
        self.assertTrue(postfix_valid(post))

    def test_pow_neg(self):
        exp = '~ 3 ^ 2'
        post = infix_to_postfix(exp)
        self.assertEqual(post, '3 2 ^ ~')
        self.assertEqual(postfix_eval(post), -9)
        self.assertTrue(postfix_valid(post))

    # def test_syntax_err(self):
    #     exp1 = '( ( 3'
        # self.assertRaises(SyntaxError, infix_to_postfix, exp1)

    def test_div_by_zero(self):
        exp = '3 0 /'
        self.assertRaises(ZeroDivisionError, postfix_eval, exp)

    def test_sample_cases(self):
        infix_file = 'sample_infix_expressions_021320.txt'
        postfix_file = 'sample_postfix_expressions_021320.txt'
        post_eval = 'postfix_eval.txt'
        in_list = []
        post_list = []
        ans = []
        with open(infix_file) as infix:
            for line in infix:
                in_list.append(line)
        with open(postfix_file) as post:
            for line in post:
                post_list.append(line)
        with open(post_eval) as evals:
            for line in evals:
                ans.append(line)
        num_exp = len(in_list)
        for i in range(num_exp):
            self.assertTrue(postfix_valid(post_list[i]))
            self.assertEqual(infix_to_postfix(in_list[i]), post_list[i].strip('\n'))
            # print(ans[i][-3:])
            # print(ans[i][:-3:])
            # if post_expr % 1 == 0.0:
            #     post_expr = int(post_expr)
            post_expr = postfix_eval(post_list[i])
            post_expr = str(post_expr)
            if post_expr[-2:] == '.0':
                post_expr = post_expr[:-2:]
            self.assertEqual(post_expr, ans[i].strip('\n'))


if __name__ == '__main__':
    unittest.main()
