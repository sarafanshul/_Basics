#![allow(non_snake_case)]
#![allow(non_camel_case_types)]
// #![allow(warnings)]
extern crate time;
use std::time::{Instant};

fn prime_sieve(max_number_to_check: usize) -> u32 {
    let mut prime_mask = vec![true; max_number_to_check];
    prime_mask[0] = false;
    prime_mask[1] = false;
    let mut total_primes_found = 0;
    const FIRST_PRIME_NUMBER: usize = 2;

    for p in FIRST_PRIME_NUMBER..max_number_to_check {
        if prime_mask[p] {
            total_primes_found += 1;
            let mut i = 2 * p;
            while i < max_number_to_check {
                prime_mask[i] = false;
                i += p;
            }
        }
    }
    total_primes_found
}

fn main() {
    let n: usize = 1e7f64 as i64 as usize;
    let now = Instant::now();
    let np = prime_sieve(n);
	println!("Time elapsed = {:?} , Primes = {} ",now.elapsed() , np);

}

// 1e7 in  6.274231131s
