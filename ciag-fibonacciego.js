function Fibonacci(n) {
		if(n < 2) return n;
		let a = 0, b = 1;
        for (let i = 2; i <= n; i++) {
            b += a;
            a = b-a;
        }
        return b;
	}

	for(i = 0; i < 30; i++) console.log(Fibonacci(i));
