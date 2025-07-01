{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "74ccdc04-0761-4982-a849-c607c2e08769",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the number : 35\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "35 is odd \n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"enter the number :\"))\n",
    "if num%2 !=1:  # num%2==0\n",
    "    print(num, \"is even\")\n",
    "else:\n",
    "    print(num, \"is odd \")\n",
    "    \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f9299d5e-193a-4224-9999-89b86826c580",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a: 65\n",
      "enter b: 90\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "largest : 90\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"enter a:\"))\n",
    "b = int(input(\"enter b:\"))\n",
    "if a>b:\n",
    "    print(\"smallest :\",a)\n",
    "elif a<b:\n",
    "    print(\"smallest :\",b)\n",
    "else:\n",
    "    print(\"both numbers are equal\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b09a1a05-e9bf-480a-9586-9c7bc00227c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a: 45\n",
      "enter b: 49\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "smallest : 49\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"enter a:\"))\n",
    "b = int(input(\"enter b:\"))\n",
    "if a<b:\n",
    "    print(\"smallest :\",a)\n",
    "elif a>b:\n",
    "    print(\"smallest :\",b)\n",
    "else:\n",
    "    print(\"both numbers are equal\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2771cdf2-0555-42ac-b032-47b52bb4676b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a: 454\n",
      "enter b: 567\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "smallest : 454\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"enter a:\"))\n",
    "b = int(input(\"enter b:\"))\n",
    "if a<b:\n",
    "    print(\"smallest :\",a)\n",
    "elif a>b:\n",
    "    print(\"smallest :\",b)\n",
    "else:\n",
    "    print(\"both numbers are equal\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b011bb82-14e5-47a9-a3da-310fe99e0d92",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "cannot assign to expression here. Maybe you meant '==' instead of '='? (2288377486.py, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[9], line 4\u001b[1;36m\u001b[0m\n\u001b[1;33m    if num%2=0:\u001b[0m\n\u001b[1;37m       ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m cannot assign to expression here. Maybe you meant '==' instead of '='?\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"enter the number\"))\n",
    "if num>0:\n",
    "    print(\"positive number\")\n",
    "    if num%2==0:\n",
    "        print(\"odd\")\n",
    "    else:\n",
    "        print(\"even\")\n",
    "else:\n",
    "    print(\"number is non-positive\")\n",
    "        \n",
    "        \n",
    "        \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "623c3716-b654-418c-80b3-0e5bf5377c91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the number 56\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "positive number\n",
      "odd\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"enter the number\"))\n",
    "if num>0:\n",
    "    print(\"positive number\")\n",
    "    if num%2==0:\n",
    "        print(\"odd\")\n",
    "    else:\n",
    "        print(\"even\")\n",
    "else:\n",
    "    print(\"number is non-positive\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4fd1a2bc-8b35-4ac6-a06b-c51b836ff422",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your 4 digit pin number: 1234\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Access Granted!!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter amount: 5000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "amount withdraw: 5000\n",
      "remaining balance: 0\n",
      "thanking you banking with HDFC......\n"
     ]
    }
   ],
   "source": [
    "ATM pin login anmd withdraw\n",
    "pin = int(input(\"enter your 4 digit pin number:\"))\n",
    "spin = 1234\n",
    "balance = 5000\n",
    "if pin == spin:\n",
    "    print(\"Access Granted!!\")\n",
    "    withdraw = int(input(\"enter amount:\"))\n",
    "    if withdraw>balance :\n",
    "        print(\"Insufficent funds!!!!\")\n",
    "    else:\n",
    "        print(\"amount withdraw:\", withdraw)\n",
    "        print(\"remaining balance:\",balance-withdraw)\n",
    "        print(\"thanking you banking with HDFC......\")\n",
    "else:\n",
    "    print(\"Access denied.....wrong pin\")\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d1d6b00-da9f-4c24-98b0-dbbf3717824e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
