#lang racket

(require net/sendmail) 

(define env (current-environment-variables))
(define email-address (environment-variables-ref env #"EMAIL"))

(send-mail-message "alex@yourEC2instance.su"  ; from forgery,
                                              ; unsure if it can get much better
                                              ; so Google doesn't spam block me
                   "Check lark!"
                   (list email-address)
                   '()
                   '()
                   '("A student is available!")
                   "")
