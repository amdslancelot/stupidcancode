from time import time

class TokenBucket:
    def __init__(self, tokens, rate):
        self.capacity = tokens
        self._tokens = tokens
        self.rate = rate
        self.timestamp = time()

    def consume(self, tokens):
        if tokens <= self._tokens:
            self._tokens -= tokens
        else:
            return False
        return True

    def get_tokens(self):
        now = time()
        if self._tokens < self.capacity:
            self._tokens += self.rate * (now - self.timestamp)
            #print "delta", (now - self.timestamp)
            self._tokens = min(self._tokens, self.capacity)
            self.timestamp = now
        return self._tokens
    tokens = property(get_tokens)

if __name__ == '__main__':
    from time import sleep
    bucket = TokenBucket(80, 10)
    print "tokens =", bucket.tokens
    print "consume(10) =", bucket.consume(10)
    print "consume(10) =", bucket.consume(10)
    #sleep(2)
    print "tokens =", bucket.tokens
    sleep(2)
    print "tokens =", bucket.tokens
    print "consume(90) =", bucket.consume(90)
    print "tokens =", bucket.tokens
