class Solution {
public:
    int divide(int dividend, int divisor) {

        unsigned int a = abs(dividend);
        unsigned int b = abs(divisor);

        int k = 0;
        unsigned int q = 0;
        bool flag = 0;

        if (((dividend < 0) && (divisor > 0))  || ((dividend > 0) && (divisor < 0)))
        {
            flag = 1;
        }


        while (a >= b)
        {

            k = 0;
            while (a >= (b<<k))
            {
                k++;
            }
            k = k - 1;
            a = a - (b<<k);

            q = q + (1<<k);

        }

        
        if (flag)
        {
            return -1*q;
        }
        else
        {
            return q;
        }

    }
};
