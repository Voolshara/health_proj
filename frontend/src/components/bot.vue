<template>
  <div class="bot">
    <p style="align-self: flex-start; font-size: 30px; margin-bottom: 0">
      Бот помощник
    </p>
    <p style="align-self: flex-start; font-size: 12px">
      Готов ответить на ваши вопросы
    </p>
    <div class="message-field">
      <el-tag
        v-for="item in all_messages"
        :key="item"
        :type="item.type"
        :class="'mess animate__animated animate__fadeIn ' + item.class"
        effect="dark"
        round
      >
        <p>{{ item.text }}</p>
      </el-tag>
    </div>
    <div class="input-field animate__animated animate__fadeIn">
      <el-input
        v-model="input_text"
        placeholder="Опишите проблему"
        autosize
        type="textarea"
        size="large"
        :rows="2"
        style="width: 80%; margin-right: 10px"
        v-if="type_problem !== null"
      />
      <el-button
        :icon="Promotion"
        circle
        v-if="type_problem !== null"
        @click="click_send"
      />

      <div v-else>
        <el-button
          v-for="button in buttons"
          :key="button.text"
          :type="button.type"
          text
          style="margin-left: 0"
          @click="click_button(button.text)"
          >{{ button.text }}</el-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import { Promotion } from "@element-plus/icons-vue";
export default {
  name: "TelegramWebApp",

  data() {
    return {
      Promotion: Promotion,
      drawer: false,
      input_text: "",
      type_problem: null,
      all_messages: [],
      buttons: [
        { type: "warning", text: "Анкеты" },
        { type: "warning", text: "Неверные данные" },
        { type: "warning", text: "Обслуживание клиентов" },
        { type: "warning", text: "Свой вопрос" },
      ],
    };
  },
  mounted() {
    setTimeout(() => {
      this.all_messages = [
        {
          text: "Здравствуйте",
          class: "mes-bot",
          type: "",
        },
      ].concat(this.all_messages);

      setTimeout(() => {
        this.all_messages = [
          {
            text: "Я готов ответить на ваши вопросы",
            class: "mes-bot",
            type: "",
          },
        ].concat(this.all_messages);

        setTimeout(() => {
          this.all_messages = [
            {
              text: "Выберите тематику вопроса:",
              class: "mes-bot",
              type: "",
            },
          ].concat(this.all_messages);
        }, 700);
      }, 700);
    }, 1500);
  },
  methods: {
    click_send() {
      let data = {
        type: this.type_problem,
        text: this.input_text,
      };
      console.log(data);
      let all_messages = [
        {
          text: this.input_text,
          class: "mes-user",
          type: "success",
        },
      ];
      this.all_messages = all_messages.concat(this.all_messages);

      this.input_text = "";

      setTimeout(() => {
        all_messages = [
          {
            text: "Отправлено",
            class: "mes-bot",
            type: "",
          },
        ];
        this.all_messages = all_messages.concat(this.all_messages);

        all_messages = [
          {
            text: "Спасибо за обратную связь!",
            class: "mes-bot",
            type: "",
          },
        ];
        this.all_messages = all_messages.concat(this.all_messages);
      }, 3000);
    },

    click_button(type) {
      this.type_problem = type;
      let all_messages = [
        {
          text: type,
          class: "mes-user",
          type: "success",
        },
      ];
      this.all_messages = all_messages.concat(this.all_messages);
      setTimeout(() => {
        all_messages = [
          {
            text: "Опишите вашу проблему:",
            class: "mes-bot",
            type: "",
          },
        ];
        this.all_messages = all_messages.concat(this.all_messages);
      }, 1500);
    },
  },
};
</script>

<style lang="scss">
.bot {
  width: 100%;
  display: flex;
  flex-direction: column;

  .message-field {
    height: 50vh;
    display: flex;
    flex-direction: column-reverse;
    align-items: flex-end;
    margin-bottom: 10px;

    .mess {
      height: 30px;

      p {
        margin-bottom: 0;
        margin: 2px;
        white-space: normal;
      }
    }

    .mes-user {
      align-self: flex-end;
      margin: 13px;
    }

    .mes-bot {
      align-self: flex-start;
      margin: 5px;
    }
  }

  .input-field {
    justify-content: center;
    align-items: center;
    width: 100%;
  }
}
</style>
