<template>
  <div class="w-full mx-auto">
    <h1 class="text-2xl font-bold text-gray-800 mb-4">Payment / Checkout</h1>
    <div class="bg-white rounded-xl shadow p-6">
      <form class="flex flex-col gap-4">
        <input
          type="text"
          placeholder="Cardholder Name"
          class="border border-gray-300 rounded-lg p-3"
        />
        <input
          type="text"
          placeholder="Card Number"
          class="border border-gray-300 rounded-lg p-3"
        />
        <div class="flex gap-4">
          <input
            type="text"
            placeholder="MM/YY"
            class="border border-gray-300 rounded-lg p-3 w-1/2"
          />
          <input
            type="text"
            placeholder="CVC"
            class="border border-gray-300 rounded-lg p-3 w-1/2"
          />
        </div>
        <button
          type="submit"
          class="px-4 py-2 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition"
        >
          Pay Now
        </button>
      </form>
      <div class="mt-6 border-t pt-4">
        <h2 class="text-lg font-semibold mb-2">Order Summary</h2>
        <div class="flex justify-between text-gray-700 mb-1">
          <span>Course:</span><span>Vue Mastery</span>
        </div>
        <div class="flex justify-between text-gray-700 mb-1">
          <span>Total:</span><span>$49.00</span>
        </div>
        <div class="text-green-600 font-bold mt-2">Payment Successful!</div>
      </div>
    </div>
  </div>
</template>
