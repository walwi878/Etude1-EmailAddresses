@author William Wallace
@date 17/05/2020


EXPLANATION
Etude 1 - Emails is a problem that checks for valid emails from stdin, and attempts to make the emails valid if they are not already. 

HOW TO RUN
To run Etude 1, open VSCode or a similar code editor and run by typing "python .\myEmailsFinal.py" without quotation marks while in the directory containing myEmailsFinal.
To check for email validity, type an email. 
If the email is invalid, program will identify one fault with the email, and print the original email and tell you why it is invalid. 
If the email can be fixed or was already vaild, the updated email will be outputted to the terminal.

For parsing a txt file with multiple emails, ensure the file contains one email per line. 
In a code editor, type "cat <text-filename-here> | python myEmailsFinal.py" without quotation marks, and replacing the file in the pointy brackets. 

For more information, refer to the PDF outlining "Etude 1 - Emails Addresses" in the current folder. 

TEST CASES:

a@a_dot_dot_b.cs.com
adsasadsadsad@sdsadasd.com
sdasd@d_ddd.com
andrew_at_[139_dot_80_dot_91_dot_50]
a@a_dot_dot_b.cs.com
andrew_at_trotman_at_c_dot_com
axe._bow@cs.com
andrew@cs.co.us
a$b@cs.com
axe__bow@cs.com
andrew_dot_trotman_at_c_dot_com
CEO@InsuroCorp.com
maffu@cs.otago.ac.nz
gerry_at_research.techies_dot_co.uk
bob.gmail.com
cath@[139.80.91.50]
bob@gmail.co.co
a@a_dot_dot_b.cs.com
adsasadsadsad@sdsadasd.com
sdasd@d_ddd.com
zade@.me.com
zade2.@me.com
zade3@me.com.
gucci-gang@gucci-gang.com
dot.s@test1.com
double..dots@test2.com
.leadingdot@test3.com
trailingdot.@test4.com
hy-phen@test5.com
-leading@hyphen.com
trailing-@hyphen.com
double--hyphen@gmail.com
Under_score@gmail.com
_leadingunderscore@gmail.com
trailingunderscore_@gmail.com
double__underscore@me.com
all.of-them_together@wackoome.com
doob90@gmail.com
dot.and-hyphen@gmail.com
dot.and_underscore@gmail.com
hyphen-and_underscore@gmail.com
--hype@gmail.com
this.tests-everything_that_at_shouldwork_dot_com
axe_.dotbro@gmail.com
Axe-.bow@gmail.com
jen@[192_dot_168_dot_178_dot_1]
jen@[192_dot_168_dot_178_dot_1].com
jen@[192_dot_168_dot_178_dot_1]@[192.178.143.22]
jen@[192_dot_16a_dot_178_dot_11222]
lau@[123.123.11.2]
a@a_dot_b_dot_c.cs.com
shoot^box@gmail.com
nice_dot_dot_domain_at_cs_dot_com
this_dot__dot_is@broken.com
andrew_dot_trotman_at_me_at_c_dot_com
a@a_dot_a_dot_dot_a_dot_dot_b.cs.com
jen@[192_dot_168_dot_178_dot_1]
jen@[192_dot_168_dot_178_dot_1].com
jen@[192_dot_168_dot_178_dot_1]@[192.178.143.22]
jen@[192_dot_16a_dot_178_dot_11222]
lau@[123.123.11.2]
a@a_dot_b_dot_c.cs.com
shoot^box@gmail.com
nice_dot_dot_domain_at_cs_dot_com
this_dot__dot_is@broken.com
andrew_dot_trotman_at_me_at_c_dot_com
a@a_dot_a_dot_dot_a_dot_dot_b.cs.com
hilton@ok.com
@.com
.com
@
 
 .com
 123.com
 com. com